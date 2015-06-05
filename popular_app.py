import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpe.settings')
import random
import string
import django
django.setup()
from faker import Factory
from app.models import (Estado, Vendedor, Sucursal, Handheld,
    TipoIncidente, Incidente, ModalidadVendedor, MyUser)


def popular():
    flush_base()
    crear_superuser()
    crear_usuarios()
    crear_estados()
    crear_sucursales()
    agregar_handhelds()
    crear_modalidades_vendedor()
    agregar_vendedores()
    crear_tipos_incidente()
    agregar_incidentes()


def flush_base():
    print("Limpiando la base actual...")
    #os.system("/home/nahuel/Code/inspt_tp_final_cpe/manage.py flush --noinput --no-initial-data")
    os.system("./manage.py flush --noinput --no-initial-data")

def crear_superuser():
    print("Creando superuser...")
    MyUser.objects.create_superuser('admin', 'admin')

def crear_usuarios():
    print("Creando usuarios...")
    MyUser.objects.create_user('test', 'test')
    MyUser.objects.create_user('demo', 'demo')
    MyUser.objects.create_user('prueba1', 'prueba1')
    MyUser.objects.create_user('prueba2', 'prueba2')
    MyUser.objects.create_user('prueba3', 'prueba3')

def crear_estados():
    print("Creando estados...")
    estados = ('operativo', 'backup', 'fuera de servicio', 'en reparacion',
               'a reparar', 'robo')
    for estado in estados:
        e = Estado.objects.create(nombre=estado)


def crear_sucursales():
    print("Creando sucursales...")
    faker = Factory.create()
    sucursales = ('alvarado', 'bahia blanca', 'cordoba', 'mar del plata', 'mendoza', 'neuquen', 'posadas', 'resistencia', 'rosario', 'san juan', 'santa fe', 'tucuman')
    for sucursal in sucursales:
        codigo = ''.join(random.choice(string.digits) for _ in range(4))
        try:
            suc = Sucursal.objects.create(nombre=sucursal, codigo=codigo)
        except IntegrityError as e:
            pass


def agregar_handhelds():
    print("Agregando handhelds...")
    faker = Factory.create()
    modelos = ('palm', 'hp', 'qtek', 'htc', 'sony', 'dell' ,'intermec', 'trimble', 'honeywell', 'symbol')
    estados = Estado.objects.all()
    sucursales = Sucursal.objects.all()
    for i in range(0, 20):
        numero_de_serie = faker.md5()[0:11]
        modelo = faker.random_element(modelos)
        estado = faker.random_element(estados)
        sucursal = faker.random_element(sucursales)
        Handheld.objects.get_or_create(
            numero_de_serie=numero_de_serie,
            modelo=modelo,
            estado=estado,
            sucursal=sucursal
        )


def crear_modalidades_vendedor():
    print("Creando modalidades de vendedor...")
    modalidades = ('remoto', 'local')
    for modalidad in modalidades:
        m = ModalidadVendedor.objects.create(nombre=modalidad)


def agregar_vendedores():
    print("Agregando vendedores...")
    faker = Factory.create()
    modalidades = ModalidadVendedor.objects.all()
    for i in range(0, 5):
        legajo = ''.join(random.choice(string.digits) for _ in range(8))
        modalidad = faker.random_element(modalidades)
        nombre = faker.first_name()
        apellido = faker.last_name()
        Vendedor.objects.get_or_create(
            legajo=legajo,
            modalidad=modalidad,
            nombre=nombre,
            apellido=apellido
        )


def crear_tipos_incidente():
    print("Creando tipos de incidente...")
    tipos = ('comunicacion', 'hardware', 'otros')
    for tipo in tipos:
        t = TipoIncidente.objects.create(nombre=tipo)


def agregar_incidentes():
    print("Agregando incidentes...")
    faker = Factory.create()
    tipos = TipoIncidente.objects.all()
    handhelds = Handheld.objects.all()
    vendedores = Vendedor.objects.all()
    usuarios = MyUser.objects.filter(is_admin=False)
    for i in range(0, 50):
        tipo = faker.random_element(tipos)
        descripcion = faker.text()
        solucion = faker.text()
        handheld = faker.random_element(handhelds)
        vendedor = faker.random_element(vendedores)
        usuario = faker.random_element(usuarios)
        fecha_carga = faker.date_time_between(
            start_date="-5d",
            end_date="now"
        )
        Incidente.objects.get_or_create(
            tipo=tipo,
            descripcion=descripcion,
            solucion=solucion,
            handheld=handheld,
            vendedor=vendedor,
            fecha_carga=fecha_carga,
            usuario=usuario
        )


if __name__ == '__main__':
    print ("Ejecutando el script para popular la base...\n")
    popular()
    print("\nBase populada!")
