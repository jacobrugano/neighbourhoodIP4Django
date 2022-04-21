from django.urls import path
from . import views


urlpatterns = [
    path('', views.neighbourhood, name='neighbourhood'),
    path('neighbourhoodview/<str:pk>/', views.view_neighbourhood, name='neighbourhoodview'),
    path('add/', views.add_neighbourhood, name='add')

]