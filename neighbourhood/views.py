from django.shortcuts import render

# Create your views here.
def neighbourhood(request):
    return render(request, 'neighbourhood/neighbourhood.html')


def add_neighbourhood(request):
    return render(request, 'neighbourhood/add_neighbourhood.html')


def view_neighbourhood(request):
    return render(request, 'neighbourhood/view_neighbourhood.html')