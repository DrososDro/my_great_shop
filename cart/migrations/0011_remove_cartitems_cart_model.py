# Generated by Django 4.2.2 on 2023-07-23 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cartitems_cart_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='cart_model',
        ),
    ]
