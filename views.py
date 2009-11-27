# Create your views here.
from util import render_to_response, write_to_response
from models import Movie


def filmes(request):
    filmes = Movie.objects.all()
    return render_to_response("admin/mygriffith/filmes.html", {'filmes': filmes}, request)



