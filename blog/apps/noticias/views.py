from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria, Comment, Usuario
from django.views.generic.list import ListView #para las vistas clases
from .forms import NoticiaForm, CommentForm
# Create your views here.

#VISTA CON FUNCIONES
def ListarNoticias(request):
    contexto = {} #diccionario
    id_categoria = request.GET.get("id", None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() #SELECT * FROM Noticias / lista objetos

    contexto['noticias'] = n

    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre
    contexto['categorias'] = cat

    return render(request, 'noticias/listar.html', contexto)

#VISTA CON CLASES
class mostrarNoticia(ListView):
    model = Noticia
    template_name = 'noticias/listarNoticia.html'

'''def DetalleNoticias(request, pk):
    contexto = {} #diccionario

    n = Noticia.objects.get(pk = pk) # 1 solo objeto

    contexto['noticia'] = n

    return render(request, 'noticias/detalle.html', contexto)
'''

def DetalleNoticias(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    comments = noticia.comments.all()

    #BORRAR NOTICIA
    if request.method == 'POST' and 'delete_noticia' in request.POST:
        noticia.delete()
        return redirect('noticias:listar')

    # COMENTARIO
    if request.method == 'POST' and 'add_comment' in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.noticia = noticia
            comment.author = request.user
            comment.save()
            return redirect('noticias:detalle', pk=pk)
    else:
        form = CommentForm()

    context = {
        'noticia': noticia,
        'comments': comments,
        'form': form,
    }
    return render(request, 'noticias/detalle.html', context)
# BORRAR COMENTARIOS
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user.username:
        comment.delete()
    return redirect('noticias:detalle', pk=comment.noticia.pk)

# AÑADIR COMENTARIOS
@login_required
def add_comment(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.user.username
        # creacion de comentario
        Comment.objects.create(noticia=noticia, author=author, text=text)
    return redirect('noticias:detalle', pk=noticia_id)


@login_required
def AddNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.author = request.user #autor de la noticia
            noticia.save()
            return redirect('home')
    else:
        form = NoticiaForm()
    
    return render(request, 'noticias/addNoticia.html', {'form': form})


