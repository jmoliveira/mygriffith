# Create your views here.
from util import render_to_response, write_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from models import Movie


#def filmes(request):
#    filmes = Movie.objects.all()
#   return render_to_response("admin/mygriffith/filmes.html", {'filmes': filmes}, request)


def buscar_filmes(request):
    generos = [('todos','Todos'), ('acao','acao'), ('comedia','comRRdia'), ('drama', 'drama')]
    filmes = []        
    
    if request.method == "POST":    
        genero = request.POST.get('genero')
        filme = request.POST.get('filme')
        if filme and genero:
            filmes = Movie.objects.filter(Q(o_title__contains=filme) | Q(title__contains=filme) & Q(genre=genero))
        elif genero:
            filmes = Movie.objects.filter(Q(genre=genero))
        else:
            filmes = Movie.objects.filter(Q(o_title__contains=filme) | Q(title__contains=filme)) 
    else:
        pass                    

    return render_to_response("admin/mygriffith/buscar_filmes.html", {'filmes': filmes, 'generos':generos}, request)

def filmes(request):
    filme_list = Movie.objects.all()
    paginator = Paginator(filme_list, 15) # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        filmes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        filmes = paginator.page(paginator.num_pages)

    return render_to_response("admin/mygriffith/buscar_filmes.html", {'filmes': filmes}, request)


def comentarios(request, id_filme):
    #import pdb; pdb.set_trace()
    filme = Movie.objects.get(id=id_filme)

    return render_to_response("admin/mygriffith/comentarios.html", {'filme': filme}, request)

