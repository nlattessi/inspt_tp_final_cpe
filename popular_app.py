omport os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpe.settings')

import django
django.setup()

from faker import Factory

from django.contrib.auth.models import User
from app.models import (Estado, Vendedor, CentroDistribucion,
    Handheld, Impresora, Incidente)

def populate():
    faker = Factory.create()
    
    for i in range(0,3):
        add_estado(nombre=faker.word())
    
    for i in range(0,5):
        add_vendedor(legajo=faker.unix_time(), nombre=faker.first_name(), apellido=faker.last_name())

    for i in range(0,10):
        add_centro_distribucion(nombre=faker.city())

    for i in range(0,20):
        add_handheld(numero_de_serie=faker.md5(),
            modelo=faker.word(),
            marca=faker.word())

    for i in range(0, 20):
        add_impresora(numero_de_serie=faker.md5(),
            modelo=faker.word(),
            marca=faker.word())

    for i in range(0, 50):
        add_incidente(descripcion=faker.text(),
            solucion=faker.text())


def add_estado(nombre):
    e = Estado.objects.get_or_create(nombre=nombre)[0]
    return e

def add_vendedor(legajo, nombre, apellido):
    v = Vendedor.objects.get_or_create(legajo=legajo, nombre=nombre, apellido=apellido)
    return v

def add_centro_distribucion(nombre):
    cd = CentroDistribucion.objects.get_or_create(nombre=nombre)
    return cd

def add_handheld(numero_de_serie, modelo, marca):
    h = Handheld.objects.get_or_create(numero_de_serie=numero_de_serie,
        modelo=modelo,
        marca=marca,
        estado=Estado.objects.order_by('?')[0],
        vendedor=Vendedor.objects.order_by('?')[0],
        centro_distribucion=CentroDistribucion.objects.order_by('?')[0])

def add_impresora(numero_de_serie, modelo, marca):
    h = Impresora.objects.get_or_create(numero_de_serie=numero_de_serie,
        modelo=modelo,
        marca=marca,
        estado=Estado.objects.order_by('?')[0],
        vendedor=Vendedor.objects.order_by('?')[0],
        centro_distribucion=CentroDistribucion.objects.order_by('?')[0])

def add_incidente(descripcion, solucion):
    i = Incidente.objects.get_or_create(descripcion=descripcion,
        solucion=solucion,
        handheld=Handheld.objects.order_by('?')[0],
        impresora=Impresora.objects.order_by('?')[0],
        vendedor=Vendedor.objects.order_by('?')[0],
        usuario=User.objects.get(username='admin'))


if __name__ == '__main__':
    print ("Starting CPE population script...")
    populate()
