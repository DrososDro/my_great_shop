# Generated by Django 4.2.2 on 2023-07-10 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variationscategory',
            old_name='variation_category',
            new_name='name',
        ),
    ]
