# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-06 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hu', '0002_youtubecodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicturesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='pictures',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pictures',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hu.PicturesCategory'),
        ),
    ]
