# Generated by Django 4.2.2 on 2023-07-10 14:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleProductImages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_slug', models.SlugField(blank=True, default=None, max_length=200, null=True, unique=True)),
                ('product_id', models.CharField(max_length=200)),
                ('alternative_product_ids', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_star_ratio', models.FloatField(default=0)),
                ('total_votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttrs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('price_b2b', models.FloatField(default=0)),
                ('is_available', models.BooleanField(default=False)),
                ('offer_duration', models.DateTimeField(blank=True, default=0, null=True)),
                ('offer_discount', models.IntegerField(blank=True, default=0, null=True)),
                ('discount', models.IntegerField(default=0)),
                ('weight', models.IntegerField(blank=True, default=0, null=True)),
                ('height', models.IntegerField(blank=True, default=0, null=True)),
                ('width', models.IntegerField(blank=True, default=0, null=True)),
                ('depth', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
