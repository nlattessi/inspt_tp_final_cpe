# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150517_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidente',
            name='fecha_carga',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 18, 22, 36, 11, 761880, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='handheld',
            name='fecha_ultimo_cambio',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='impresora',
            name='fecha_ultimo_cambio',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
