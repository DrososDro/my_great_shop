# Generated by Django 4.2.2 on 2023-07-07 20:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('variations', '0002_alter_variations_variation_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationsCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('variation_category', models.CharField(choices=[('color', 'Color'), ('size', 'Size'), ('material', 'Material'), ('contition', 'Contition'), ('product_origin', 'Product Origin')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='variations',
            name='variation_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variations.variationscategory'),
        ),
    ]
