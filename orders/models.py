from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

#my apps import
from product.models import Product
from human.models import Client, Profile
from .utils import generate_code


class Position(models.Model):
    """Instancia de uma encomenda"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)

    created = models.DateTimeField(blank=True)
    
    def save(self, *args, **kwargs):
        self.price = self.product.price * float(self.quantity)
        return super().save(*args, **kwargs)
    
    def get_order_id(self):
        """reverse relation com Encomenda"""
        order_obj = self.order_set.first()
        return order_obj.id

    def __str__(self):
        return f'{self.id}, produto: {self.product.name}, quantidade: {self.quantity}'

class Order(models.Model):
    """Encomenda: 1 encomenda tem varios instancias denominadas positions"""

    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Preço total {self.total_price} euros'

    def get_absolute_url(self):
        return reverse('orders:detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        if self.transaction_id == '':
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()


class CSV(models.Model):
    
    file_name = models.CharField(max_length=100, null=True)
    csv_file = models.FileField(upload_to='csvs', null=True)
    activated = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)


