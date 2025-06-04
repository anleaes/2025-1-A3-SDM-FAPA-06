from django.db import models
from Equipamento.models import Equipamento
#from orders.models import Order
# Create your models here.

class Orderitem(models.Model):
    quantity = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.DecimalField('Preco unitario', max_digits=10, decimal_places=2)
    Equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    
    
    class Meta:
        unique_together = ('order', 'product')
        verbose_name = 'Equipamento de Pedido'
        verbose_name_plural = 'Equipamentos de Pedidos'
        ordering =['id']

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"