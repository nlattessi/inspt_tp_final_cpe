# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150518_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandheldCambioEstado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha_cambio', models.DateTimeField(auto_now=True)),
                ('estado_anterior', models.ForeignKey(related_name='estadio_anterior', to='app.Estado')),
            ],
        ),
        migrations.RemoveField(
            model_name='vendedor',
            name='centro_distribucion',
        ),
        migrations.AddField(
            model_name='handheld',
            name='centro_distribucion',
            field=models.ForeignKey(blank=True, to='app.CentroDistribucion', null=True),
        ),
        migrations.AddField(
            model_name='impresora',
            name='centro_distribucion',
            field=models.ForeignKey(blank=True, to='app.CentroDistribucion', null=True),
        ),
        migrations.AddField(
            model_name='handheldcambioestado',
            name='handheld',
            field=models.ForeignKey(to='app.Handheld'),
        ),
        migrations.AddField(
            model_name='handheldcambioestado',
            name='nuevo_estado',
            field=models.ForeignKey(related_name='nuevo_estado', to='app.Estado'),
        ),
    ]
