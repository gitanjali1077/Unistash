# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0002_delete_viewers'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
            ],
        ),
    ]
