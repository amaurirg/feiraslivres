import csv
import os

from django.core.serializers import serialize
from django.db import IntegrityError
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from feiraslivres.settings import BASE_DIR
from .models import FeirasLivres
from .serializers import FeirasLivresSerializer, FeirasLivresPutSerializer
import logging


logger = logging.getLogger('core.views')


def index(request):
    logger.debug(request.body)
    return render(request, 'index.html')


class FeirasLivresBusca(APIView):
    serializer_class = FeirasLivresSerializer

    def get(self, request, args1, args2, format=None):
        if args1 == 'regiao5' or args1 == 'regiao8':
            args2 = args2.title()
        else:
            args2 = args2.upper()
        serializer = self.serializer_class(FeirasLivres.objects.raw(
            f"SELECT * FROM feiraslivres WHERE {args1} = '{args2}'"), many=True)
        logger.debug(f"Realizada consulta por {args1} = {args2} status=200.")
        return Response(serializer.data)


class FeirasLivresLista(APIView):
    serializer_class = FeirasLivresSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(FeirasLivres.objects.all(), many=True)
        logger.debug(f'Consulta Lista status=200.')
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f"Nova feira Registro:{request.data['registro']} "
                         f"Nome da Feira:{request.data['nome_feira']} "
                         f"status:{status.HTTP_201_CREATED} criada com sucesso.""")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeiraLivre(APIView):
    serializer_class = FeirasLivresPutSerializer

    def get_object(self, registro):
        try:
            return FeirasLivres.objects.get(registro=registro)
        except FeirasLivres.DoesNotExist:
            raise Http404

    def get(self, request, registro, format=None):
        feira = self.get_object(registro)
        logger.debug(f"Consulta Registro:{registro} status=200.")
        serializer = FeirasLivresPutSerializer(feira)
        return Response(serializer.data)

    def put(self, request, registro, format=None):
        feira = self.get_object(registro)
        serializer = FeirasLivresPutSerializer(feira, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f"Registro {registro} Nome:{request.data['nome_feira']} "
                         f"status:202 alterado com sucesso.")
            return Response(serializer.data)
        logger.error(f"Tentativa de alteração do registro:{request.data['registro']} "
                     f"Nome:{request.data['nome_feira']} status:304 falhou.")
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED, exception=False)

    def delete(self, request, registro, format=None):
        feira = self.get_object(registro)
        feira.delete()
        logger.debug(f"Registro:{feira.registro} Nome:{feira.nome_feira} "
                     f"status:204 deletado com sucesso.")
        return Response(status=status.HTTP_204_NO_CONTENT)


def popula_banco(request):
    arquivo_csv = (os.path.abspath("docs/DEINFO_AB_FEIRASLIVRES_2014.csv"))

    file = open(arquivo_csv)
    fileReader = csv.reader(file)
    dados_csv = list(fileReader)

    dados = [
        FeirasLivres(long = row[1], lat = row[2], setcens = row[3], areap = row[4], coddist = row[5],
                     distrito = row[6], codsubpref = row[7], subprefe =row[8], regiao5 = row[9],
                     regiao8 = row[10], nome_feira = row[11], registro = row[12], logradouro = row[13],
                     numero = row[14], bairro =row[15], referencia = row[16]) for row in dados_csv[1::]]

    try:
        FeirasLivres.objects.bulk_create(dados)
        return HttpResponse("Dados importados com sucesso!")

    except IntegrityError:
        return HttpResponse("O banco já foi populado!")
