# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-23 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
