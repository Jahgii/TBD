# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-06 23:28
from __future__ import unicode_literals

import Blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20180201_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[Blog.models.validate_author_email]),
        ),
    ]
