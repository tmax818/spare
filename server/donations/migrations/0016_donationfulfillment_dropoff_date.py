# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0015_phone_number_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationfulfillment',
            name='dropoff_date',
            field=models.DateField(null=True),
        ),
    ]