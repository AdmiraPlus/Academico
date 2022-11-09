"""academico URL Configuration (URLs Comunes o Generales)

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
	PasswordResetCompleteView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
	
    path('', views.inicio, name='inicio' ),
	path('usuario/registrar/', views.registrar_usuario, name='registrar_usuario'),
	path('sesion/iniciar/', views.iniciar_sesion, name='iniciar_sesion'),
	path('sesion/cerrar/', views.cerrar_sesion, name='cerrar_sesion'),
	
	#	path('registro/', views.registro, name='registro'),
	
	path('password/reset/', PasswordResetView.as_view(template_name='password-reset.html'), name='password_reset'),
	path('password/reset/done/', PasswordResetDoneView.as_view(template_name="password-reset-done.html"), name='password_reset_done'),
	path('password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='password-confirm.html'), name='password_reset_confirm'),
	path('password/reset/complete/', PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), name='password_reset_complete'),
	
    path('xxx_registrar_usuario/', views.xxx_registrar_usuario),
	
    path('', include('apps.academico.urls'))
]
