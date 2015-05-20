# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150515_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handheld',
            name='centro_distribucion',
        ),
        migrations.RemoveField(
            model_name='handheld',
            name='vendedor',
        ),
        migrations.RemoveField(
            model_name='impresora',
            name='centro_distribucion',
        ),
        migrations.RemoveField(
            model_name='impresora',
            name='vendedor',
        ),
        migrations.AddField(
            model_name='vendedor',
            name='centro_distribucion',
            field=models.ForeignKey(to='app.CentroDistribucion', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='handheld',
            field=models.OneToOneField(to='app.Handheld', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='impresora',
            field=models.OneToOneField(to='app.Impresora', blank=True, null=True),
        ),
    ]
