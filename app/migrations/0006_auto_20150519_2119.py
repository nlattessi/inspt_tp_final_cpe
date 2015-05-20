# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150519_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpresoraCambioEstado',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fecha_cambio', models.DateTimeField(auto_now=True)),
                ('estado_anterior', models.ForeignKey(to='app.Estado', related_name='impresora_estadio_anterior')),
                ('impresora', models.ForeignKey(to='app.Impresora')),
                ('nuevo_estado', models.ForeignKey(to='app.Estado', related_name='impresora_nuevo_estado')),
            ],
        ),
        migrations.AlterField(
            model_name='handheldcambioestado',
            name='estado_anterior',
            field=models.ForeignKey(to='app.Estado', related_name='handheld_estadio_anterior'),
        ),
        migrations.AlterField(
            model_name='handheldcambioestado',
            name='nuevo_estado',
            field=models.ForeignKey(to='app.Estado', related_name='handheld_nuevo_estado'),
        ),
    ]
