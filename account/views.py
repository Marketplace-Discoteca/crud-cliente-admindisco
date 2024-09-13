# views.py
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ClienteSignUpForm, AdministradorSignUpForm
from .models import User, Cliente, Administrador
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def cliente_register(request):
    if request.method == 'POST':
        form = ClienteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = ClienteSignUpForm()
    return render(request, 'signup_cliente.html', {'form': form})

def administrador_register(request):
    if request.method == 'POST':
        form = AdministradorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = AdministradorSignUpForm()
    return render(request, 'signup_admin.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                # Verificamos si es cliente o administrador
                if user.is_admindisco is False and user.is_superuser is False:
                    return redirect('cliente_panel')
                elif user.is_admindisco and user.is_superuser is False:
                    return redirect('admin_panel')
                else:
                    messages.error(request, 'Usted es SuperUsuario')
            else:
                messages.error(request, 'Credenciales incorrectas')
        else:
            messages.error(request, 'Información de login no válida')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def cliente_panel(request):
    return render(request, 'cliente_panel.html')

@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')


from .serializer import UserSerializer, ClienteSerializer, AdministradorSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

