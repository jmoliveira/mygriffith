# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models

from models import Movie

   
NUM_PER_PAGE = 10

class MovieAdmin(admin.ModelAdmin):
    list_display = ('o_title', 'title', 'rating' )
    search_fields = ('o_title', 'title')
    list_per_page = NUM_PER_PAGE
    fieldsets = (
        (None, {
            'fields': ('number', 'seen', 'title', 'o_title', 'director',  'genre', 'year', 'runtime', 'rating', 'o_site', 'site', 'trailer', 'plot', 'notes', 'country')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('image', 'ratio_id', 'collection_id', 'volume_id', 'medium_id', 'vcodec_id', 'poster_md5', 'loaned', 'color', 'cond', 'layers', 'region', 'media_num', 'width', 'height', 'barcode', 'screenplay', 'cameraman', 'studio', 'classification', 'cast')
        }),
    )

 

admin.site.register(Movie, MovieAdmin)
