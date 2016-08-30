# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 11:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shoppingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 11, 52, 25, 476542), null=True)),
                ('product_status', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('product_detail_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=45, null=True)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 11, 52, 25, 477097), null=True)),
                ('product_image', models.ImageField(default=None, max_length=500, upload_to=b'images/product_images/', verbose_name=b'Image')),
                ('product_status', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=1)),
                ('product_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Shoppingapp.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 11, 52, 25, 476078), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 11, 52, 25, 475581), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 11, 52, 25, 474659), null=True),
        ),
    ]
