# Generated by Django 5.0.1 on 2024-01-28 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_production_production_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='product',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Produto'),
        ),
    ]