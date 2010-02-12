# Create your views here.
from util import render_to_response, write_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from models import Movie
from forms import SearchMovieForm

def paginacao_filmes(filmes, request, qtd=10):
    
    paginator = Paginator(filmes, qtd)
    
    try:
        page = int(request.POST.get('page', '1'))
    except ValueError:
        page = 1
    #import pdb; pdb.set_trace()
    print "PAGE:", page
    #print "filmes:", filmes

    try:
        filmes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        filmes = paginator.page(paginator.num_pages)

    return filmes

def buscar_filmes(request):
    if request.method == 'POST':
        form = SearchMovieForm(request.POST)
        qs_filmes = None
        #import pdb; pdb.set_trace()
        if form.is_valid():
            genero = form.cleaned_data['genero']
            filme = form.cleaned_data['filme']
            if filme and genero:
                if Movie.GENEROS_CHOICES.get_key_default() in genero:
                    qs_filmes = Movie.objects.filter(Q(o_title__contains=filme) | Q(title__contains=filme))
                else:
                    qs_filmes = Movie.objects.filter(Q(o_title__contains=filme) | Q(title__contains=filme) & Q(genre__in=genero))    
            elif genero:
                if Movie.GENEROS_CHOICES.get_key_default() in genero:
                    qs_filmes = Movie.objects.all()
                else:
                    qs_filmes = Movie.objects.filter(Q(genre__in=genero))
            elif filme:
                qs_filmes = Movie.objects.filter(Q(o_title__contains=filme) | Q(title__contains=filme)) 
            
            if qs_filmes:
                filmes = paginacao_filmes(qs_filmes, request)
            else:
                filmes = None

        return render_to_response("admin/mygriffith/buscar_filmes.html", {'form': form, 'filmes': filmes}, request)

    else:
        form = SearchMovieForm()
        return render_to_response("admin/mygriffith/buscar_filmes.html", {'form': form}, request)


def comentarios(request, id_filme):
    #import pdb; pdb.set_trace()
    filme = Movie.objects.get(id=id_filme)

    return render_to_response("admin/mygriffith/comentarios.html", {'filme': filme}, request)

