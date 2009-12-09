# -*- coding: utf-8 -*-
from django import forms
from models import Movie

class SearchMovieForm(forms.Form):
    filme = forms.CharField(label=u'Filme', required=True)    
    genero =  forms.MultipleChoiceField(label=u'Genero', choices=Movie.GENEROS_CHOICES, required=False, initial='todos')
    

