# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-15 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200410_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('balls', 'Balls'), ('dmd', 'DMD'), ('gloves', 'Gloves'), ('other', 'Other')], default='balls', max_length=10),
        ),
    ]
