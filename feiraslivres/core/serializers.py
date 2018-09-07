from rest_framework import serializers
from .models import FeirasLivres


class FeirasLivresSerializer(serializers.ModelSerializer):

    class Meta:

        model = FeirasLivres
        fields = '__all__'

    def create(self, validated_data):
        """
        Cria uma nova feira retornando os novos dados
        :param validated_data:
        """
        return FeirasLivres.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Atualiza uma feira retornando os novos dados
        """

        instance.id = validated_data.get('id', instance.id)
        instance.long = validated_data.get('long', instance.long)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.setcens = validated_data.get('setcens', instance.setcens)
        instance.areap = validated_data.get('areap', instance.areap)
        instance.coddist = validated_data.get('coddist', instance.coddist)
        instance.distrito = validated_data.get('distrito', instance.distrito)
        instance.codsubpref = validated_data.get('codsubpref', instance.codsubpref)
        instance.subprefe = validated_data.get('subprefe', instance.subprefe)
        instance.regiao5 = validated_data.get('regiao5', instance.regiao5)
        instance.regiao8 = validated_data.get('regiao8', instance.regiao8)
        instance.nome_feira = validated_data.get('nome_feira', instance.nome_feira)
        instance.registro = validated_data.get('registro', instance.registro)
        instance.logradouro = validated_data.get('logradouro', instance.logradouro)
        instance.numero = validated_data.get('numero', instance.numero)
        instance.bairro = validated_data.get('bairro', instance.bairro)
        instance.referencia = validated_data.get('referencia', instance.referencia)
        instance.save()
        return instance
