from django.urls import path
from . import views

urlpatterns = [
    path(
        "asian/",
        views.restaurants,
        {"category": "asian"},
        name="asian",
    ),
    path(
        "european/",
        views.restaurants,
        {"category": "european"},
        name="european",
        
    ),
    path(
        "african/",
        views.restaurants,
        {"category": "african"},
        name="african",
    ),
    path(
        "irish/",
        views.restaurants,
        {"category": "irish"},
        name="irish",
    ),
    path(
        "american/",
        views.restaurants,
        {"category": "american"},
        name="american",
    ),


]
