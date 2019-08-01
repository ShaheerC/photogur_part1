from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import *

def pictures_root(request):
    return HttpResponseRedirect("/pictures")

def pictures_html(request):
    context = { 'pictures': Picture.objects.all() }
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}
    return render(request, 'picture.html', context)

def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {'pictures': search_results, 'query': query}
    return render(request, 'search.html', context)

def create_comment(request):
    picture_id = request.POST['picture']
    picture = Picture.objects.filter(id=picture_id)[0]
    name = request.POST['name']
    comment = request.POST['comment']
    new_comment = Comment(name=name, message=comment, picture=picture)
    new_comment.save()
    return HttpResponseRedirect(f'/pictures/{picture_id}')