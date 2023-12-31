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
    """
    This is a function for submitting a restaurant review.
    it takes in request and restaurant_id and renders
    review_page.html.
    """
    restaurant = Restaurant.objects.get(RestaurantId=restaurant_id)
    ratings = Review.objects.filter(restaurant=restaurant)
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            restaurant_rating = rating_form.save(commit=False)
            restaurant_rating.restaurant = restaurant
            profile.reviewed.add(restaurant)
            restaurant_rating.user = user
            restaurant_rating.save()
            messages.success(
                request, f"{user.username} you have reviewed {restaurant}"
            )
            return redirect(
                reverse(
                    "allreviews", kwargs={'restaurant_id': restaurant_id}
                    )
                )
        else:
            messages.error(
                request,
                "Please rate all the criterias before submiting.",
            )
    else:
        rating_form = RatingForm()

    context = {
        'restaurant': restaurant,
        'ratings': ratings,
        'user': user,
        'rating_form': rating_form,
    }
    return render(request, 'review/review_page.html', context)


@login_required()
def allreviews(request, restaurant_id):
    """
    This function is to show all reviews to user.
    Takes in args request and restaurant_id and renders
    allreviews.html
    """
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    reviews = Review.objects.filter(restaurant=restaurant)
    context = {
        "restaurant": restaurant,
        "reviews": reviews,
    }
    return render(request, "review/allreviews.html", context)


@login_required()
def edit_review(request, restaurant_id, review_id):
    """
    This function is for editing an review. The review already done is
    prepopulated when opening the review form when user wants to edit.
    Changes made is then saved.
    """
    user = request.user
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    review = get_object_or_404(Review, id=review_id)
    user_review = Review.objects.filter(restaurant=restaurant, user=user)

    if user_review.exists() or user.is_superuser:
        user_reviewed = True
    else:
        user_reviewed = False

    if review.user != user and not user.is_superuser:
        messages.error(request, "You are not authorized to edit this review.")
        return redirect(
            reverse(
                "allreviews", kwargs={'restaurant_id': restaurant_id}
                )
            )
    if request.method == "POST":
        rating_form = RatingForm(request.POST, instance=review)
        if rating_form.is_valid():
            restaurant_rating = rating_form.save(commit=False)
            restaurant_rating.save()
            messages.success(
                request, f"{user.username} your review has been updated"
            )

            return redirect(
                reverse(
                    "allreviews", kwargs={'restaurant_id': restaurant_id}
                    )
                )
        else:
            messages.error(
                request,
                "something went wrong.",
            )
    else:
        rating_form = RatingForm(instance=review)

    context = {
        "rating_form": rating_form,
        "review": review,
        "restaurant": restaurant,
        "user_reviewed": user_reviewed,
    }

    return render(request, "review/review_page.html", context)


def profile_reviews(request, restaurant_id):

    """
    This function checks if user has previously reviewed the restaurant
    """
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    review = get_object_or_404(Review, user=user, restaurant=restaurant)
    if review:
        if restaurant in profile.reviewed.all():
            return redirect(
                reverse(
                    "edit_review", args=[restaurant_id, review.id]
                    )
                )


@login_required()
def delete_review(request, restaurant_id, review_id):
    """
    This function handles deleting of review for a particular restaurant.
    """
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    review = get_object_or_404(Review, id=review_id)
    user = request.user

    if not user.is_superuser and review.user != user:
        messages.error(
            request, "You are not authorized to delete this review."
        )
        return redirect(
            reverse(
                "allreviews", kwargs={'restaurant_id': restaurant_id}
                )
            )

    profile = Profile.objects.get(user=review.user)
    if review.restaurant in profile.reviewed.all():
        profile.reviewed.remove(review.restaurant)

    review.delete()
    if user.is_superuser:
        messages.success(
            request,
            f"{review.user}'s review for {restaurant} has been deleted "
        )
    else:
        messages.success(
            request,
            f"Your review for {restaurant} has been deleted {user.username}"
        )
    return redirect(
        reverse(
            "allreviews", kwargs={'restaurant_id': restaurant_id}
            )
        )
