# Generated by Django 4.2.2 on 2023-07-10 14:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationsCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('variation_category', models.CharField(choices=[('color', 'Color'), ('size', 'Size'), ('material', 'Material'), ('contition', 'Contition'), ('product_origin', 'Product Origin')], max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Variations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('variation_value', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('variation_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variations.variationscategory')),
            ],
        ),
    ]
