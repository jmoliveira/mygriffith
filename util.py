from django.http import HttpResponseRedirect, HttpResponse, Http404


def render_to_response(template, context, request=None):
    from django.shortcuts import render_to_response
    from django.template import RequestContext
    
    context_instance = None
    if request:
        context_instance = RequestContext(request)

    return render_to_response(template, context, context_instance)

def write_to_response(text, mimetype='text/plain', status=200):
    return HttpResponse(text, mimetype=mimetype, status=status)
