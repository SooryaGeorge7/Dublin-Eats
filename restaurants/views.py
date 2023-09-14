
import os
from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from .models import Restaurant
from review.models import Restaurant, Review
from users.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import NoReverseMatch


GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")


def get_place_details(place_id):
    """
    This function retrieves details from google places API
    using place_id
    """
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "website,photos",
        "key": GOOGLE_PLACES_API_KEY,
    }
    response = requests.get(details_url, params=params)
    details_data = response.json()
    return details_data.get("result", {})


def restaurants(request, category):
    """
    View function to retrieve and display restaurants results.
    It takes in a cattegory  as parameter to retrieve restaurant information
    from google places API which is then displayed in categories.html

    """
    if category == "asian":

        url = (
            f"https://maps.googleapis.com/maps/api/place/"
            f"textsearch/json?query=Asian%20restaurants%20in%20Dublin"
            f"&key={GOOGLE_PLACES_API_KEY}"
        )
    elif category == "european":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch"
            f"/json?query=European%20restaurants%20in%20Dublin"
            f"&key={GOOGLE_PLACES_API_KEY}"
        )
    elif category == "african":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch"
            f"/json?query=African%20restaurants%20in%20Dublin"
            f"&key={GOOGLE_PLACES_API_KEY}"
        )
    elif category == "irish":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/"
            f"json?query=Irish%20restaurants%20in%20Dublin"
            f"&key={GOOGLE_PLACES_API_KEY}"
        )
    elif category == "american":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/"
            f"json?query=American%20restaurants%20in%20Dublin"
            f"&key={GOOGLE_PLACES_API_KEY}"
        )
    else:
        pass
    restaurants = []
    response = requests.get(url)
    restaurant_data = response.json()
    results = restaurant_data.get("results", [])
    user = request.user
    paginator = Paginator(results, 8)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    for result in page_object:
        place_id = result.get("place_id")
        if place_id:
            details_data = get_place_details(place_id)
            website_url = details_data.get("website", "")
            photos = details_data.get("photos", "")
            image_urls = []
            if photos:
                for photo in photos:
                    photo_reference = photo.get('photo_reference')
                    if photo_reference:
                        image_url = (
                            f"https://maps.googleapis.com/maps/api/"
                            f"place/photo?maxwidth=400"
                            f"&photoreference={photo_reference}"
                            f"&key={GOOGLE_PLACES_API_KEY}"
                        )
                        image_urls.append(image_url)
            else:
                image_urls.append("https://res.cloudinary.com/dif9bjzee"
                                  f"/image/upload/v1692544795/"
                                  "default-image_kyuezj.webp")

        try:
            # Try to retrieve the restaurant from the database
            restaurant_details = Restaurant.objects.get(RestaurantId=place_id)
            # Category is updated even if restaurant exists in database.
            restaurant_details.category = category
            restaurant_details.save()
        except Restaurant.DoesNotExist:
            # If the restaurant does not exist,Restaurant object is created
            restaurant_details = Restaurant(
                name=result["name"],
                website=website_url,
                category=category,
                address=result["formatted_address"],
                RestaurantId=place_id,
            )
            print(restaurant_details)
            restaurant_details.save()

        pinned = False
        user_reviewed = False
        if request.user.is_authenticated:
            user_review = Review.objects.filter(
                restaurant=restaurant_details, user=user
            )
            profile = Profile.objects.get(user=user)
            if user_review.exists():
                user_reviewed = True
            if (
                profile.pinned_restaurants
                .filter(RestaurantId=place_id)
                .exists()
            ):
                pinned = True

        restaurants.append({
            "name": result["name"],
            "category": category,
            "address": result["formatted_address"],
            "image_urls": image_urls,
            "user_reviewed": user_reviewed,
            "pinned": pinned,
            "website_url": website_url,
            "place_id": place_id,
        })

    return render(request, 'restaurants/categories.html', {
        "restaurants": restaurants,
        "page_object": page_object,
        "restaurant_details": restaurant_details,
        })


@login_required()
def to_visit(request, restaurant_id):
    """
    This function allows authenticated users to add or remove
    restaurants from their list of pinned restaurants and then
    redirects them to the appropriate page. It also includes messages
    to inform the user of the action taken.
    """
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if restaurant in profile.pinned_restaurants.all():
        profile.pinned_restaurants.remove(restaurant)
        messages.success(
            request,
            f"{user.username} you have removed {restaurant} from your profile",
        )
    else:
        profile.pinned_restaurants.add(restaurant)
        messages.success(
            request,
            f"{user.username} you have pinned {restaurant} to your profile",
        )

    try:
        category_url = reverse(restaurant.category)
    except NoReverseMatch:
        return redirect("searchresults", restaurant.category)

    return redirect(category_url)


@login_required()
def remove_pin(request, restaurant_id):
    """
    This function allows authenticated users to remove a restaurant from
    their list of pinned restaurants and then redirects them to their
     profile page with a success message indicating the removal.
    """
    restaurant = get_object_or_404(Restaurant, RestaurantId=restaurant_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if restaurant in profile.pinned_restaurants.all():
        profile.pinned_restaurants.remove(restaurant)
        messages.success(
            request,
            f"{user.username} you have removed {restaurant}"
            f" from your profile",
        )
    return redirect("profile", username=user.username)
