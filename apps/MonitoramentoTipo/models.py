from django.db import models

# Create your models here.

class MonitoramentoTipo(models.Model):
    quantity = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    description = models.TextField('Descricao', max_length=100)
    security = models.TextField('Seguranca', max_length=100)
    rate_security = models.TextField('Grau de Seguranca', max_length=100)
    
    class Meta:
        verbose_name = 'Monitoramento Tipo'
        verbose_name_plural = 'Monitoramento Tipos'
        ordering =['id']

    def __str__(self):
        return self.name
