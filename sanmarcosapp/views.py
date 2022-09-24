from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from sanmarcosapp.models import Administrativos, Facultades, Directorios
from sanmarcosapp.forms import FacultadForm, AdministrativoForm, DirectorioForm, UserEditForm
from django.shortcuts import render, get_object_or_404, redirect
from . models import Administrativos

# Create your views here.


def index(request):
    return render(request, "sanmarcosapp/index.html")

# @login_required


def about(request):
    return render(request, "sanmarcosapp/about.html")


def facultades(request):
    facultades = Facultades.objects.all()
    diccionario2 = {
        'facultades': facultades
    }
    return render(request, "sanmarcosapp/facultades.html", diccionario2)


def administrativos(request):
    administrativos = Administrativos.objects.all()
    diccionario = {
        'administrativos': administrativos
    }
    return render(request, "sanmarcosapp/administrativos.html", diccionario)


def directorios(request):
    directorios = Directorios.objects.all()
    dic = {
        'directorios': directorios
    }
    return render(request, "sanmarcosapp/directorios.html", dic)


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "sanmarcosapp/logeado.html", {"mensaje": f"Bienvenido {usuario}"})

            else:
                return render(request, "sanmarcosapp/Errorlogin.html", {"mensaje": "Error, datos incorrectos"})

        else:
            return render(request, "sanmarcosapp/Errorlogin.html", {"mensaje": "Error, formulario erróneo"})

    form = AuthenticationForm()

    return render(request, 'sanmarcosapp/login.html', {"form": form})


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "sanmarcosapp/index.html", {"mensaje": "Usuario creado"})

    else:
        form = UserCreationForm()

    return render(request, "sanmarcosapp/registro.html", {"form": form})


def logout(request):
    logout(request)
    return redirect('sanmarcosapp/logout.html')


def buscar_administrativo(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
    if nombre:
        administrativos = Administrativos.objects.filter(
            nombre__icontains=nombre)
        return render(request, 'sanmarcosapp/administrativos.html', {'administrativos': administrativos})
    else:
        print('Nada para mostrar')
        return request(request, 'sanmarcosapp/administrativos.html', {})


@login_required
def alta_directorio(request):
    if request.method == "POST":
        mi_form = DirectorioForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            directorio = Directorios(
                nombre=datos["nombre"], contacto=datos["contacto"])
            directorio.save()
        return redirect("directorios.html")
    return render(request, "sanmarcosapp/alta_directorios.html")


@login_required
def alta_administrativo(request):
    if request.method == "POST":
        mi_form = AdministrativoForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            administrativo = Administrativos(
                nombre=datos["nombre"], cargo=datos["cargo"])
            administrativo.save()
        return redirect("administrativos.html")
    return render(request, "sanmarcosapp/alta_administrativos.html")


@login_required
def alta_facultad(request):
    if request.method == "POST":
        mi_form = FacultadForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            facultad = Facultades(
                nombre=datos["nombre"], escuelas=datos["escuelas"])
            facultad.save()
        return redirect("facultades.html")
    return render(request, "sanmarcosapp/alta_facultades.html")


def editar_directorios(request, id):
    directorio = Directorios.objects.get(id=id)

    if request.method == 'POST':
        miform = DirectorioForm(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            directorio.nombre = datos['nombre']
            directorio.contacto = datos['contacto']
            directorio.save()
            return redirect('/')
    else:
        miform = DirectorioForm(
            initial={'nombre': directorio.nombre, 'contacto': directorio.contacto})

    return render(request, "sanmarcosapp/editar_directorios.html", {'miform': miform, 'directorio': directorio})


@login_required
def eliminar_directorio(request, id):
    directorio = get_object_or_404(Directorios, pk=id)

    if directorio:
        directorio.delete()

    return redirect('directorios.html')


@login_required
def eliminar_facultad(request, id):
    facultad = Facultades.objects.get(id=id)
    facultad.delete()

    facultades = Facultades.objects.all()

    return render(request, "sanmarcosapp/facultades.html", {"facultades": facultades})


@login_required
def eliminar_administrativo(request, id):
    administrativo = get_object_or_404(Administrativos, pk=id)

    if administrativo:
        administrativo.delete()

    return redirect('administrativos.html')


def detalles_facultades(request, id):

    facultades = Facultades.objects.filter(id=id)

    return render(request, "sanmarcosapp/detalles_facultades.html", {"facultades": facultades})


def detalles_directorios(request, id):

    directorios = Directorios.objects.filter(id=id)

    return render(request, "sanmarcosapp/detalles_directorios.html", {"directorios": directorios})


def detalles_administrativos(request, id):

    administrativos = Administrativos.objects.filter(id=id)

    return render(request, "sanmarcosapp/detalles_administrativos.html", {"administrativos": administrativos})


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return redirect('/')
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "sanmarcosapp/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


@login_required
def editar_administrativos(request, id):
    administrativo = Administrativos.objects.get(id=id)

    if request.method == 'POST':
        miform = AdministrativoForm(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            administrativo.nombre = datos['nombre']
            administrativo.cargo = datos['cargo']
            administrativo.save()
            return redirect('/')
    else:
        miform = AdministrativoForm(
            initial={'nombre': administrativo.nombre, 'cargo': administrativo.cargo})

    return render(request, "sanmarcosapp/editar_administrativos.html", {'miform': miform, 'administrativo': administrativo})


@login_required
def editar_facultades(request, id):
    facultad = Facultades.objects.get(id=id)

    if request.method == 'POST':
        miform = FacultadForm(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            facultad.nombre = datos['nombre']
            facultad.escuelas = datos['escuelas']
            facultad.save()
            return redirect('/')
    else:
        miform = FacultadForm(
            initial={'nombre': facultad.nombre, 'escuelas': facultad.escuelas})

    return render(request, "sanmarcosapp/editar_facultades.html", {'miform': miform, 'facultad': facultad})


def oficinas(request):
    return render(request, "sanmarcosapp/oficinas.html")
