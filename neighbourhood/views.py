from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http  import Http404, HttpResponse
import datetime as dt
from .models import Neighborhood, Profile, Business, Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def neighbourhood(request):
    neighbors = Neighborhood.objects.all()
    return render(request, 'neighbourhood/neighbourhoods.html', {'neighbors':neighbors})


def view_neighbourhood(request, pk):
    view_neighbors = Neighborhood.objects.get(id=pk)
    return render(request, 'neighbourhood/neighbourhoodview.html', {'view_neighbors':view_neighbors})



def add_post(request):
    posts = Post.objects.all()
    return render(request, 'neighbourhood/add_post.html', {'posts':posts})
