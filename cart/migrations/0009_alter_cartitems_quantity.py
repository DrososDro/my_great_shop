# Generated by Django 4.2.2 on 2023-07-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]