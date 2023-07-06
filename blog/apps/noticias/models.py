from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    #para imagen debemos instalar pillow
    imagen = models.ImageField(upload_to= 'noticias') 
