# Generated by Django 4.2.2 on 2023-07-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variations', '0002_rename_variation_category_variationscategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variations',
            name='variation_value',
            field=models.CharField(max_length=200),
        ),
    ]
