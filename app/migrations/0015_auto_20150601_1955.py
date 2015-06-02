# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20150601_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidente',
            name='fecha_carga',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
