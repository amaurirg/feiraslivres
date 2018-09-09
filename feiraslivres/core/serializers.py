from rest_framework import serializers
from .models import FeirasLivres


class FeirasLivresSerializer(serializers.ModelSerializer):

    class Meta:

        model = FeirasLivres
        fields = '__all__'


class FeirasLivresPutSerializer(serializers.ModelSerializer):

    class Meta:

        model = FeirasLivres
        fields = '__all__'
        read_only_fields = ('registro',)
