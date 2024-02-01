from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from .models import Product, Inventary, Production, ProductionOrder




@receiver(post_save, sender=Product)
def create_inventary(sender, instance, created, **kwargs):
    if created:
        Inventary.objects.create(product=instance, total_quantity=0)

@receiver(post_save, sender=Production)
@receiver(post_delete, sender=Production)
def update_inventory(sender, instance, **kwargs):
    production_order = instance.production_order
    inventory = Inventary.objects.get(product=production_order.product)
    
    # Atualiza a quantidade no inventário
    inventory.total_quantity = production_order.production_set.aggregate(Sum('quantity'))['quantity__sum'] or 0
    inventory.save()
    
    # Atualiza a quantidade produzida na ordem de produção
    production_order.quantity_produced = inventory.total_quantity
    production_order.save()