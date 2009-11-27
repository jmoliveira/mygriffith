<html>
<head>
	<title>Jota Videoteca</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="/media/mygriffith/css/gray.css" />
</head>
<body>

<!-- ITEMS -->
{% for filme in filmes %} 

<table id="filme_{{ filme.id }}">
    {% if filme.image %}
	<tr class="image">
		<td rowspan="11">
			<img src="./posters/" alt="XIIIII" />
		</td>
	</tr>
    {% endif %}
	<tr class="title"> 
		<th>Título no Brasil</th>
		<td>{{ filme.title }}</td>
	</tr>
	<tr class="otitle">
		<th>Título Original</th>
		<td>{{ filme.otitle }}</td>
	</tr>
	<tr class="director">
		<th>Diretor</th>
		<td>{{ filme.director }}</td>
	</tr>
	<tr class="genre">
		<th>Genero</th>
		<td>{{ filme.genre }}</td>
	</tr>
	<tr class="year">
		<th>Ano</th>
		<td>{{ filme.year }}</td>
	</tr>
	<tr class="runtime">
		<th>@TITLE@</th>
		<td>{{ filme.runtime }}</td>
	</tr>
	<tr class="rating">
		<th>Duração</th>
		<td>{{ filme.rating }}{% if filme.rating %} min {% endif %}</td>
	</tr>
	<tr class="links">
		<th>o_site</th>
		<td>{% if filme.o_site %}<a href="{{ filme.o_site }}">{{ filme.o_site }}</a>{% endif %}</td>
	</tr>
	<tr class="links">
		<th>site</th>
		<td>{% if filme.site %}<a href="{{ filme.site }}">{{ filme.site }}</a>{% endif %}</td>
	</tr>
	<tr class="links">
		<th>Trailer</th>
		<td>{% if filme.trailer %}<a href="{{ filme.trailer }}">{{ filme.trailer }}</a>{% endif %}</td>
	</tr>
	<tr class="plot">
		<th>Sinopse</th>
		<td>{{ filme.plot }}</td>
	</tr>
</table>
{% endfor %} 

<!-- /ITEMS -->


</body>
</html>
