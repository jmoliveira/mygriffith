from django.db import models

class Movie(models.Model):
    GENEROS_CHOICES = (('todos', 'Todos'), ('acao', 'acao'), ('comedia', 'comedia'), ('drama', 'drama'))

    id = models.AutoField(primary_key=True, db_column='movie_id') 
    number = models.PositiveIntegerField(verbose_name=u'Num', max_length=11, null=True, blank=False)
    o_title = models.CharField(verbose_name=u'Titulo Original', max_length=256, null=True, blank=True)
    title = models.CharField(verbose_name=u'Titulo Brasil', max_length=256, null=True, blank=True)
    seen = models.PositiveIntegerField(verbose_name=u'seen', max_length=1, null=True, blank=True)
    plot = models.TextField(verbose_name=u'plot', null=True, blank=True)
    notes = models.TextField(verbose_name=u'notes', null=True, blank=True)
    image = models.CharField(verbose_name=u'image', max_length=128, null=True, blank=True)
    rating = models.PositiveIntegerField(verbose_name=u'Rating', max_length=6, null=True, blank=True)
    year = models.PositiveIntegerField(verbose_name=u'year', max_length=6, null=True, blank=True)
    o_site = models.CharField(verbose_name=u'o_site', max_length=256, null=True, blank=True)
    site = models.CharField(verbose_name=u'site', max_length=256, null=True, blank=True)
    trailer = models.CharField(verbose_name=u'trailer', max_length=256, null=True, blank=True)
    country = models.CharField(verbose_name=u'country', max_length=128, null=True, blank=True)
    genre = models.CharField(verbose_name=u'genre', max_length=128, null=True, blank=True)
    runtime = models.PositiveIntegerField(verbose_name=u'runtime', max_length=6, null=True, blank=True)
    director = models.CharField(verbose_name=u'director', max_length=256, null=True, blank=True)

    ratio_id = models.PositiveIntegerField(verbose_name=u'ratio_id', max_length=11, null=True, blank=True)
    collection_id = models.PositiveIntegerField(verbose_name=u'collection_id', max_length=11, null=True, blank=True)
    volume_id = models.PositiveIntegerField(verbose_name=u'volume_id', max_length=11, null=True, blank=True)
    medium_id = models.PositiveIntegerField(verbose_name=u'medium_id', max_length=11, null=True, blank=True)
    vcodec_id = models.PositiveIntegerField(verbose_name=u'vcodec_id', max_length=11, null=True, blank=True)
    poster_md5 = models.CharField(verbose_name=u'poster_md5', max_length=32, null=True, blank=True)
    loaned = models.PositiveIntegerField(verbose_name=u'loaned', max_length=1, null=True, blank=True)
    color = models.PositiveIntegerField(verbose_name=u'color', max_length=6, null=True, blank=True)
    cond = models.PositiveIntegerField(verbose_name=u'cond', max_length=6, null=True, blank=True)
    layers = models.PositiveIntegerField(verbose_name=u'layers', max_length=6, null=True, blank=True)
    region = models.PositiveIntegerField(verbose_name=u'region', max_length=6, null=True, blank=True)
    media_num = models.PositiveIntegerField(verbose_name=u'media_num', max_length=6, null=True, blank=True)
    width = models.PositiveIntegerField(verbose_name=u'width', max_length=6, null=True, blank=True)
    height = models.PositiveIntegerField(verbose_name=u'height', max_length=6, null=True, blank=True)
    barcode = models.CharField(verbose_name=u'barcode', max_length=32, null=True, blank=True)
    screenplay = models.CharField(verbose_name=u'screenplay', max_length=256, null=True, blank=True)
    cameraman = models.CharField(verbose_name=u'cameraman', max_length=256, null=True, blank=True)
    studio = models.CharField(verbose_name=u'studio', max_length=128, null=True, blank=True)
    classification = models.CharField(verbose_name=u'classification', max_length=128, null=True, blank=True)
    cast = models.TextField(verbose_name=u'cast', null=True, blank=True)


    def __unicode__(self):
        return unicode(self.number)
    
    class Meta:
        verbose_name = u'Filme'
        verbose_name_plural = u'Filmes'
        db_table = 'movies'
        ordering = ('number',)

