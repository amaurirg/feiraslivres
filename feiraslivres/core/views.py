from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import FeirasLivres
from .serializers import FeirasLivresSerializer


def index(request):
    return render(request, 'index.html')


class FeirasLivresLista(generics.ListCreateAPIView):

    queryset = FeirasLivres.objects.all()
    serializer_class = FeirasLivresSerializer


class FeiraLivre(generics.RetrieveUpdateDestroyAPIView):

    queryset = FeirasLivres.objects.all()
    serializer_class = FeirasLivresSerializer
