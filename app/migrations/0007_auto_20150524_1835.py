# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150519_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impresora',
            name='centro_distribucion',
        ),
        migrations.RemoveField(
            model_name='impresora',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='impresoracambioestado',
            name='estado_anterior',
        ),
        migrations.RemoveField(
            model_name='impresoracambioestado',
            name='impresora',
        ),
        migrations.RemoveField(
            model_name='impresoracambioestado',
            name='nuevo_estado',
        ),
        migrations.RemoveField(
            model_name='incidente',
            name='impresora',
        ),
        migrations.RemoveField(
            model_name='vendedor',
            name='impresora',
        ),
        migrations.DeleteModel(
            name='Impresora',
        ),
        migrations.DeleteModel(
            name='ImpresoraCambioEstado',
        ),
    ]
