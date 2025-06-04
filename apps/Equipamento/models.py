from django.db import models
from ClasseEquipamento.models import ClasseEquipamento

# Create your models here.

class Equipamento(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    Modelo = models.CharField('Modelo', max_length=50)
    Price = models.DecimalField('Preco', max_digits=10, decimal_places=2)
    ClasseEquipamento = models.ForeignKey(ClasseEquipamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering =['id']

    def __str__(self):
        return self.name
    

    