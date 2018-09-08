from django.core.serializers import serialize
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FeirasLivres
from .serializers import FeirasLivresSerializer
import logging


logger = logging.getLogger('core.views')


def index(request):
    logger.debug(request.body)
    return render(request, 'index.html')


# class FeirasLivresLista(generics.ListCreateAPIView):
#
#     queryset = FeirasLivres.objects.all()
#     serializer_class = FeirasLivresSerializer
#     logger.debug('Feiras Livres')

'''
class FeiraLivre(generics.RetrieveUpdateDestroyAPIView):

    queryset = FeirasLivres.objects.all()
    serializer_class = FeirasLivresSerializer
'''

class FeirasLivresLista(APIView):
    serializer_class = FeirasLivresSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(FeirasLivres.objects.all(), many=True)
        logger.debug(f'Consulta Lista {status.HTTP_200_OK}')
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f"Nova feira criada Registro:{request.data['registro']} "
                         f"Nome da Feira:{request.data['nome_feira']} status:{status.HTTP_201_CREATED}.""")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeiraLivre(APIView):
    serializer_class = FeirasLivresSerializer

    def get_object(self, pk):
        try:
            return FeirasLivres.objects.get(pk=pk)
        except FeirasLivres.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        feira = self.get_object(pk)
        serializer = FeirasLivresSerializer(feira)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        feira = self.get_object(pk)
        serializer = FeirasLivresSerializer(feira, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f"Registro {request.data['registro']} Nome:{request.data['nome_feira']} "
                        f"status:202 alterado com sucesso.")
            return Response(serializer.data)
        logger.error(f"Tentativa de alteração do registro:{request.data['registro']} "
                     f"Nome:{request.data['nome_feira']} status:304 falhou.")
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk, format=None):
        feira = self.get_object(pk)
        print(feira.registro)
        # print(feira['id'])
        feira.delete()
        logger.debug(f"Registro:{feira.registro} Nome:{feira.nome_feira} "
                     f"status:204 deletado com sucesso.")
        return Response(status=status.HTTP_204_NO_CONTENT)