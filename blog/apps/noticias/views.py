from django.shortcuts import render

# Create your views here.
def listarNoticias(request):
    return render(request, 'noticias/listar.html')