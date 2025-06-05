from django.db import models
from Cliente.models import Cliente

# Create your models here.

class Client(models.Model):
    
    address = models.CharField('Endereco', max_length=200)  
    LOCATION_CHOICES = (
        ('Casa'),
        ('Predio'),
        ('Empresa'),
        ('Outro'),
    )
    Location = models.CharField('Localização', max_length=1, choices=LOCATION_CHOICES)
    Cliente = models.ManyToManyField(Cliente, verbose_name="Cliente")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name