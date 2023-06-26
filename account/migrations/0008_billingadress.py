# Generated by Django 4.2.2 on 2023-06-26 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_account_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('address_line_1', models.CharField(blank=True, max_length=100)),
                ('address_line_2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('billing_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to=settings.AUTH_USER_MODEL)),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
