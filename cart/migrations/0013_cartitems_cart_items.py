# Generated by Django 4.2.2 on 2023-07-26 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_remove_cart_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='cart_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
            preserve_default=False,
        ),
    ]
