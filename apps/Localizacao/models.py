from django.db import models


# Create your models here.

class Localizacao(models.Model):
    
    address = models.CharField('Endereco', max_length=200)  
    LOCATION_CHOICES = (
        ('Casa', 'Casa'),
        ('Apartamento', 'Apartamento'),
        ('Comercio', 'Comercio'),
        ('Industria', 'Industria'),
        ('Escola', 'Escola'),
        ('Hospital', 'Hospital'),
        ('Predio', 'Predio'),
        ('Empresa', 'Empresa'),
        ('Outro', 'Outro'),
        
    )
    Location = models.CharField('Localização', max_length=12, choices=LOCATION_CHOICES)
   

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name