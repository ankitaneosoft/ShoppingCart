# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 14:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoppingapp', '0003_auto_20160830_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='product_availability',
            field=models.CharField(choices=[(b'1', b'In Stock'), (b'0', b'Out Of Stock')], default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 14, 11, 22, 331272), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 14, 11, 22, 330780), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 14, 11, 22, 329853), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 14, 11, 22, 331725), null=True),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 30, 14, 11, 22, 332280), null=True),
        ),
    ]
