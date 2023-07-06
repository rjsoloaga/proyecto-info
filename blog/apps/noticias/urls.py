from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = { 
    path('', views.listarNoticias, name='listar')
}