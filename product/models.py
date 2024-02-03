from django.db import models
from django.utils import timezone


from human.models import Employee


class Product(models.Model):

    CATEGORY = {
    "SHIELD" : "SHIELD",
    "BRACKET" : "BRACKET",
    "ASSEMBLY" : "HANGER ASSEMBLY",
    }
    name=models.CharField(max_length=120, verbose_name='Produto')
    image=models.ImageField(upload_to='product', default='random.jpg')
    description = models.TextField(verbose_name="Descrição", default=" Sem Descrição ")
    price = models.FloatField(help_text='euros cada', verbose_name="Preço")
    category = models.CharField(max_length=20, choices=CATEGORY, blank=True, verbose_name="Categoria")
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.name} - ({self.category})'


class ProductionState(models.TextChoices):
    PENDENT = 'P', 'Pendente'
    IN_PROD = 'EA', 'Em Produção'
    CONCLUDED = 'C', 'Concluída'

class ProductionOrder(models.Model):
    """
    Ordem de produção
    Pretendo implementar a creação de uma Ordem de Produção
    a quando da chegada de uma encomenda
    verifica se há em stoque se não houver
    cria esta ordem
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True, blank=True, verbose_name='Produto')
    quantity_ordered = models.IntegerField(verbose_name= 'Quantidade da Ordem')
    quantity_produced = models.IntegerField(verbose_name='Quantidade Produzida', default = 0)
    state = models.CharField(
        max_length=2,
        choices=ProductionState.choices,
        blank= True,
        null= True,
    )
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.quantity_produced == 0:
            self.state = ProductionState.PENDENT
        elif self.quantity_produced == self.quantity_ordered:
            self.state = ProductionState.CONCLUDED
        else:
            self.state = ProductionState.IN_PROD
        
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} - Quantidade: {self.quantity_ordered} - Estado: {self.get_state_display()}'


class Production(models.Model):
    """
    Instâncias de produção:
    Necessario criar sinal que atualiza a ordem de produção
    e atualiza stoque e ecomenda
    """

    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    #machine
    quantity = models.IntegerField(verbose_name='Quantidade Produzida')
    time = models.IntegerField(verbose_name= 'Tempo de Produção')
    date = models.DateTimeField(verbose_name='Data de Produção')

    def __str__(self):
        return f'{self.employee.first_name} [{self.product}] - {self.quantity} x '

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now()
        return super().save(*args, **kwargs)

class Inventary(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_quantity = models.IntegerField(blank=True, null=True, verbose_name = 'Quantidade Total')
    productions = models.ManyToManyField(Production)

    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.product.name} - {self.total_quantity} unidades'
