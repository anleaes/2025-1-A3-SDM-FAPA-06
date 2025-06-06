from django.db import models
from Monitoramento.models import Monitoramento
from MonitoramentoTipo.models import MonitoramentoTipo

# Create your models here.

class TipoMonitoramentoTipo(models.Model):
    Monitoramento = models.ForeignKey(Monitoramento, on_delete=models.CASCADE)
    MonitoramentoTipo = models.ForeignKey(MonitoramentoTipo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'TipoMonitoramentoTipo'
        verbose_name_plural = 'Tipos de MonitoramentoTipo'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.client)