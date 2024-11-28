"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from web import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('contacto/',views.contact, name="contact"),
    path('form_success/', views.form_success, name='form_success'),
    path('login/', views.log_in, name='log_in'),
    path('signup/', views.sign_up, name='sign_up'),
    path('logout/', views.sign_out, name='logout'),
    path('cart/', views.view_cart, name='view_cart'),  # Vista del carrito de compras
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Agregar producto al carrito
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Eliminar del carrito
    path('premium/', views.premium_flan_list, name='premium_flan_list'),


]
