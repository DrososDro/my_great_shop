# Generated by Django 4.2.2 on 2023-07-16 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productattrs_condition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productattrs',
            old_name='condition',
            new_name='contition',
        ),
    ]
