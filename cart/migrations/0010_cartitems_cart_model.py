# Generated by Django 4.2.2 on 2023-07-23 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_alter_cartitems_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='cart_model',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
            preserve_default=False,
        ),
    ]
