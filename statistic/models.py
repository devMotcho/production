from django.db import models
from human.models import Employee

from product.models import Product

class ProductStatistics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    total_production_quantity = models.IntegerField(default=0, verbose_name='Total de Quantidade Produzida')
    average_production_time = models.FloatField(default=0, verbose_name='Tempo Médio de Produção por Unidade')
    production_efficiency = models.FloatField(default=0, verbose_name='Eficiência de Produção')

    def __str__(self):
        return f'{self.product.name} - Estatísticas de Produção'


class ProductionStatistics(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    total_production_quantity = models.IntegerField(default=0, verbose_name='Total de Quantidade Produzida')
    average_production_time = models.FloatField(default=0, verbose_name='Tempo Médio de Produção por Unidade')
    production_efficiency = models.FloatField(default=0, verbose_name='Eficiência de Produção')

    def __str__(self):
        return f'{self.employee.first_name} - Estatísticas de Produção'
