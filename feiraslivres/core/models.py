from django.db import models


class FeirasLivres(models.Model):

    long = models.IntegerField()
    lat = models.IntegerField()
    setcens = models.BigIntegerField()
    areap = models.BigIntegerField()
    coddist = models.PositiveSmallIntegerField()
    distrito = models.CharField(max_length=40)
    codsubpref = models.PositiveSmallIntegerField()
    subprefe = models.CharField(max_length=40)
    regiao5 = models.CharField(max_length=10)
    regiao8 = models.CharField(max_length=10)
    nome_feira = models.CharField(max_length=40)
    registro = models.CharField(max_length=6, unique=True)
    logradouro = models.CharField(max_length=70)
    numero = models.CharField(max_length=12)
    bairro = models.CharField(max_length=30)
    referencia = models.CharField(max_length=70)


    class Meta:
        verbose_name = 'Feira Livre em SP'
        verbose_name_plural = 'Feiras Livres em SP'
        ordering = ['registro']

        db_table = 'feiraslivres'

    def __str__(self):
        return self.nome_feira
