# Generated by Django 5.0.1 on 2024-01-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_productionorder_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='random.jpg', upload_to='products'),
        ),
    ]