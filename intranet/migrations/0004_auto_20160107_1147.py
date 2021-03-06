# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0003_auto_20160106_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='images/news'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='file_upload',
            field=models.FileField(upload_to='files/notices/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/posts/'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='file_upload',
            field=models.FileField(upload_to='files/resources/'),
        ),
    ]
