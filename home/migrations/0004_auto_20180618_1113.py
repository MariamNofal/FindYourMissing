# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-18 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180618_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundperson',
            name='FoundPersonImage',
            field=models.ImageField(upload_to='FoundProfiles/'),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='MissingPersonImage',
            field=models.ImageField(upload_to='MissingProfiles/'),
        ),
    ]
