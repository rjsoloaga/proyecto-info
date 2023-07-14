from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'noticias'

urlpatterns = [
    path('', views.ListarNoticias, name='listar'),
    path('listarNoticia/', views.mostrarNoticia.as_view()), #clase
    path('detalle/<int:pk>', views.DetalleNoticias, name='detalle'),
    path('addNoticia', views.AddNoticia, name='addnoticia'),
    #url comentarios
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/add/<int:noticia_id>/', views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)