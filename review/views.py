

from .forms import RatingForm
from .models import Review
from restaurants.models import Restaurant
from django.contrib.auth.models import User
from users.models import Profile
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required()
def review(request, restaurant_id):
    restaurant = Restaurant.objects.get(RestaurantId= restaurant_id)
    ratings = Review.objects.filter(restaurant=restaurant)
    user = request.user
    profile = get_object_or_404(Profile, user= user)
    
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid() :
            restaurant_rating = rating_form.save(commit=False)
            restaurant_rating.restaurant = restaurant
            profile.reviewed.add(restaurant)
            restaurant_rating.user = user
            restaurant_rating.save()
            messages.success(
                request, f"{user.username} you have reviewed {restaurant}"
            )
            return redirect("dublineats-home")
        else:
            messages.error(
                request,
                "Please fill in all fields before submitting.",
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
        "restaurant":restaurant,
        "reviews": reviews,
    }

    return render(request, "review/allreviews.html", context)

@login_required()
def edit_review(request, restaurant_id, review_id):
    user = request.user
    # restaurant = Restaurant.objects.get(RestaurantId=restaurant_id)
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    review = get_object_or_404(Review, id=review_id)
    user_review = Review.objects.filter(restaurant=restaurant, user=user)
    
    if user_review.exists():
        user_reviewed = True
    else:
        user_reviewed = False

    if review.user != user:
        messages.error(request, "You are not authorized to edit this review.")
        return redirect(reverse("allreviews"))

    if request.method == "POST":
        rating_form = RatingForm(request.POST, instance=review)
        if rating_form.is_valid():
            restaurant_rating = rating_form.save(commit=False)
            restaurant_rating.save()
            messages.success(
                request, f"{user.username} your review has been updated"
            )

            return redirect(reverse("allreviews", kwargs={'restaurant_id': restaurant_id}))
        else:
            messages.success(
                request,
                "something went wrong.",
            )
    else:
        rating_form = RatingForm(instance=review)

    context = {
        "rating_form": rating_form,
        "review":review,
        "restaurant": restaurant,
        "user_reviewed": user_reviewed,
    }

    return render(request, "review/review_page.html", context)

def profile_reviews(request, restaurant_id):
    
    #restaurant = Restaurant.objects.get(RestaurantId=restaurant_id)
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)

    user = request.user
    # profile = Profile.objects.get(user=user)
    profile = get_object_or_404(Profile, user=user)
    review = get_object_or_404(Review, user=user,restaurant=restaurant)
    if review:
        if restaurant in profile.reviewed.all():
            return redirect(reverse("edit_review", args=[restaurant_id, review.id]))

@login_required()
def delete_review(request, restaurant_id, review_id):
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    review = get_object_or_404(Review, id=review_id)
    user = request.user

    if review.user != user:
        messages.error(
            request, "You are not authorized to delete this review."
        )
        return redirect("profile")

    profile = Profile.objects.get(user=user)
    if review.restaurant in profile.reviewed.all():
        profile.reviewed.remove(review.restaurant)

    review.delete()
    messages.success(request, f"Your review has been deleted {user.username} ")

    return redirect("profile")