# Generated by Django 4.2.2 on 2023-07-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productattrs_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattrs',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used')], default='new', max_length=25),
        ),
    ]