# Generated by Django 4.2.2 on 2023-07-10 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productattrs',
            options={'ordering': ['-price']},
        ),
    ]
