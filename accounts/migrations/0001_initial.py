# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-17 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Btech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('rollno', models.CharField(max_length=10)),
            ],
        ),
    ]
