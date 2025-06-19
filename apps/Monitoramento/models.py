from django.db import models
from Cliente.models import Cliente
from Localizacao.models import Localizacao

# Create your models here.

class Monitoramento(models.Model):
    name = models.CharField('Nome', max_length=50)
    event = models.TextField('Descricao', max_length=100)
    date_time = models.DateTimeField('Data e Hora', auto_now_add=True, null=True, blank=True)
    status = models.BooleanField('Ativo', default=False)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Monitoramento'
        verbose_name_plural = 'Monitoramentos'
        ordering =['id']

    def __str__(self):
        return self.name