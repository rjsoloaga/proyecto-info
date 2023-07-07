from django.shortcuts import render
from .models import Noticia
# Create your views here.


def ListarNoticias(request):
    context = {}
    n = Noticia.objects.all()
    context['noticias'] = n
    return render(request, 'noticias/listar.html', context)

def DetalleNoticias(request, pk):
    context = {}
    n = Noticia.objects.get(pk=pk)
    context['noticia'] = n
    return render(request, 'noticias/detalle.html', context)
