# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-13 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='NewPost', error_messages={'unique': 'Este titulo no es unico, intenta de nuevo con otro titulo'}, help_text='Debe de se un titulo unico', max_length=250, unique=True, verbose_name='post title'),
        ),
    ]