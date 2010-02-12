# -*- coding: utf-8 -*-
from django import forms
from models import Movie

class SearchMovieForm(forms.Form):
    filme = forms.CharField(label=u'Filme', required=False)    
    genero =  forms.MultipleChoiceField(label=u'Genero', choices=Movie.GENEROS_CHOICES.get_choices(), required=False, initial='todos')
    

