# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0105_msg_high_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='priority',
            field=models.IntegerField(default=500, help_text='The priority for this message to be sent, higher is higher priority', null=True),
        ),
    ]
