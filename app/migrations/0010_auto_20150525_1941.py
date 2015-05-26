# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150524_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoIncidente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='handheld',
            name='marca',
        ),
        migrations.AlterField(
            model_name='handheld',
            name='numero_de_serie',
            field=models.CharField(unique=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='legajo',
            field=models.CharField(unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solo numeros.')], max_length=8),
        ),
        migrations.AddField(
            model_name='incidente',
            name='tipo',
            field=models.ForeignKey(to='app.TipoIncidente', default=1, related_name='tipo_incidente'),
            preserve_default=False,
        ),
    ]
