from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.index, name='index'),
    path('busid/',views.busnum,name='busnum'),
    path('searchroute/',views.SearchRoute,name='searchroute'),
    path('srearchbus/',views.SearchBus,name='searchbus')
]