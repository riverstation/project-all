# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
    ]
