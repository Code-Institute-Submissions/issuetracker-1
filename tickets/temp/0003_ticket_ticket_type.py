# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-21 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('BUG', 'Bug'), ('NEW FEATURE', 'New feature')], default='BUG', max_length=11),
        ),
    ]