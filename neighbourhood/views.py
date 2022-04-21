from django.shortcuts import render

# Create your views here.
def neighbourhood(request):
    return render(request, 'neighbourhood/neighbourhoods.html')




def view_neighbourhood(request, pk):
    return render(request, 'neighbourhood/neighbourhoodview.html')



def add_neighbourhood(request):
    return render(request, 'neighbourhood/add_neighbourhood.html')
