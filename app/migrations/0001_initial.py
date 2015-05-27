# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CentroDistribucion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Handheld',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('numero_de_serie', models.CharField(max_length=255, unique=True)),
                ('modelo', models.CharField(max_length=255, blank=True)),
                ('marca', models.CharField(max_length=255, blank=True)),
                ('fecha_ultimo_cambio', models.DateTimeField(auto_now_add=True)),
                ('centro_distribucion', models.ForeignKey(to='app.CentroDistribucion')),
                ('estado', models.ForeignKey(to='app.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('numero_de_serie', models.CharField(max_length=255, unique=True)),
                ('modelo', models.CharField(max_length=255, blank=True)),
                ('marca', models.CharField(max_length=255, blank=True)),
                ('fecha_ultimo_cambio', models.DateTimeField(auto_now_add=True)),
                ('centro_distribucion', models.ForeignKey(to='app.CentroDistribucion')),
                ('estado', models.ForeignKey(to='app.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descripcion', models.TextField()),
                ('solucion', models.TextField()),
                ('handheld', models.ForeignKey(to='app.Handheld', null=True, blank=True)),
                ('impresora', models.ForeignKey(to='app.Impresora', null=True, blank=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('legajo', models.CharField(max_length=255, unique=True)),
                ('nombre', models.CharField(max_length=255, blank=True)),
                ('apellido', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='incidente',
            name='vendedor',
            field=models.ForeignKey(to='app.Vendedor', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='impresora',
            name='vendedor',
            field=models.ForeignKey(to='app.Vendedor'),
        ),
        migrations.AddField(
            model_name='handheld',
            name='vendedor',
            field=models.ForeignKey(to='app.Vendedor'),
        ),
    ]
