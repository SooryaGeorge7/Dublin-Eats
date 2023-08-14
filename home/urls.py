from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dublineats-home'),
    path("search/",views.search,name="search"),
    path('searchresults/<str:category>/', views.searchresults, name= 'searchresults' ),
    
]