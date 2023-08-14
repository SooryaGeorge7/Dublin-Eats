import os
from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from review.models import Review
from restaurants.models import Restaurant
from users.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def search(request):
    category = request.GET.get("query")
    if category:
        return redirect("searchresults", category=category)
    print(category)


def searchresults(request, category):

    return 
# Create your views here.
def home(request):
    return render(request, 'home/index.html')