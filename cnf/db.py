# Archivo de configuración de Bases de Datos.


from decouple import config

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración para SQLite:
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración para PostGrSQL:
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Configuración para MySQL:
# Configuración para la web:
# 	BD: admirapl_academico
#	Usuario: admirapl_academico_admin
#	Clave: AdmiraPlus2015
MySQL_AdmiraPlus = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'HOST': 'srvadmirape',
        'PORT': '3306',
        'NAME': 'academico',
        'USER': 'root',
        'PASSWORD': 'AdmiraPlus2015',
    }
}
MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'HOST': config('HOST'),
		'PORT': config('PORT'),
		'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
    }
}