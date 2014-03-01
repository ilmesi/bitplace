from django.shortcuts import render, render_to_response, RequestContext


def index(request):
    pass

def product(request, id):
    return render_to_response('market/product.html', RequestContext(request))

def callback(request):
    pass
