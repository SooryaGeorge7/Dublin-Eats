

from .forms import RatingForm
from .models import Review
from restaurants.models import Restaurant
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required()
def review(request, restaurant_id):
    restaurant = Restaurant.objects.get(RestaurantId= restaurant_id)
    ratings = Review.objects.filter(restaurant=restaurant)
    user = request.user
    
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid() :
            restaurant_rating = rating_form.save(commit=False)
            restaurant_rating.restaurant = restaurant
            
            restaurant_rating.user = user
            restaurant_rating.save()
            messages.success(
                request, f"{user.username} you have reviewed {restaurant}"
            )
            return redirect("dublineats-home")
        else:
            messages.error(
                request,
                "something went wrong.",
            )
    else:
        rating_form = RatingForm()
    
    context = {
        'restaurant': restaurant,
        'ratings': ratings,
        'rating_form': rating_form,
    }
    return render(request, 'review/review_page.html', context)

@login_required()
def allreviews(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    reviews = Review.objects.filter(restaurant=restaurant)
    context = {
        "reviews": reviews,
    }

    return render(request, "review/allreviews.html", context)