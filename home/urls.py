from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dublineats-home'),
    path("search/",views.search,name="searchresults"),
    
    
]