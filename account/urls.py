# urls.py
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'administradores', views.AdministradorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register/cliente/', views.cliente_register, name='cliente_register'),
    path('register/administrador/', views.administrador_register, name='administrador_register'),
    path('login/', views.login_view, name='login'),
    path('cliente_panel/', views.cliente_panel, name='cliente_panel'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path("__reload__/", include("django_browser_reload.urls")),
]
