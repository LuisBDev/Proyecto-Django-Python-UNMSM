"""sanmarcosweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from sanmarcosapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about.html', views.about),
    path('index.html', views.index),
    path('login.html', views.login_request, name='Login'),
    path('registro.html', views.register, name='Register'),
    path('logout.html', LogoutView.as_view(
        template_name='sanmarcosapp/logout.html'), name='Logout'),

    # Buscadores
    path('buscar_administrativos/', views.buscar_administrativo),
    path('buscar_facultades/', views.buscar_facultad),
    path('buscar_directorios/', views.buscar_directorio),


    path('administrativos.html', views.administrativos),
    path('alta_administrativo', views.alta_administrativo,
         name='alta_administrativo'),
    path('alta_administrativos.html',
         views.alta_administrativo, name='alta_administrativo'),


    path('eliminar_administrativo_<int:id>',
         views.eliminar_administrativo, name='eliminar_administrativo'),

    path('directorios.html', views.directorios),
    path('alta_directorio', views.alta_directorio, name='alta_directorio'),
    path('alta_directorios.html', views.alta_directorio, name='alta_directorio'),


    path('eliminar_directorio_<int:id>',
         views.eliminar_directorio, name='eliminar_directorio'),

    path('facultades.html', views.facultades),
    path('alta_facultad', views.alta_facultad, name='alta_facultad'),
    path('alta_facultades.html', views.alta_facultad, name='alta_facultad'),
    path('eliminar_facultad_<int:id>',
         views.eliminar_facultad, name='eliminar_facultad'),
    path('detalles_directorios_<int:id>',
         views.detalles_directorios, name='detalles_directorios'),
    path('detalles_administrativos_<int:id>',
         views.detalles_administrativos, name='detalles_administrativos'),
    path('detalles_facultades_<int:id>',
         views.detalles_facultades, name='detalles_facultades'),
    path('editarperfil', views.editarperfil, name="editarperfil"),
    path('editarperfil.html', views.editarperfil, name="editarperfil"),
    path('editar_administrativo/<int:id>',
         views.editar_administrativos, name='editar_administrativos'),
    path('editar_facultades/<int:id>',
         views.editar_facultades, name='editar_facultades'),
    path('editar_directorios_<int:id>',
         views.editar_directorios, name='editar_directorios'),
    path('noticias.html', views.noticias),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
