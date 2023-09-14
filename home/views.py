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

GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")


def get_details(place_id):
    """
    This function retrieves details from google places API
    using place_id
    """
    detail_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "website,photos",
        "key": GOOGLE_PLACES_API_KEY,
    }
    response = requests.get(detail_url, params=params)
    detail_data = response.json()
    return detail_data.get("result", {})


def search(request):
    """
    Takes in search query from home page and redirect to searchresults url
    """
    query = request.GET.get("query")

    if query:
        return redirect("searchresults", query=query)


def searchresults(request, query):
    """
    View function to retrieve and display restaurant search results.
    It takes in query as parameter to retrieve restaurant information from
    google places API which is then displayed in results.html

    """

    query = query

    url = (
        f"https://maps.googleapis.com/maps/api/place/textsearch/json?"
        f"query={query}%20restaurants%20in%20Dublin"
        f"&type=restaurant&location=53.350140,-6.266155"
        f"&key={GOOGLE_PLACES_API_KEY}"
    )
    user = request.user
    restaurant_results = []
    response = requests.get(url)
    restaurant_data = response.json()
    results = restaurant_data.get("results", [])
    paginator = Paginator(results[:10], 8)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    for result in page_object:
        place_id = result.get("place_id")
        if place_id:
            detail_data = get_details(place_id)
            website_url = detail_data.get("website", "")
            photos = detail_data.get("photos", "")
            image_urls = []
            if photos:
                for photo in photos:
                    photo_reference = photo.get('photo_reference')
                    if photo_reference:
                        image_url = (
                            f"https://maps.googleapis.com/maps/api/place/"
                            f"photo?maxwidth=400&photoreference="
                            f"{photo_reference}&key={GOOGLE_PLACES_API_KEY}"
                        )
                        image_urls.append(image_url)
            else:
                image_urls.append("https://res.cloudinary.com/dif9bjzee/"
                                  f"image/upload/v1692544795/"
                                  f"default-image_kyuezj.webp")

        try:
            # Try to retrieve the restaurant from the database
            restaurant_details = Restaurant.objects.get(RestaurantId=place_id)
            # Category is updated even if restaurant exists in database.
            restaurant_details.category = query
            restaurant_details.save()
        except Restaurant.DoesNotExist:
            # If the restaurant does not exist,Restaurant object is created
            restaurant_details = Restaurant(
                name=result["name"],
                website=website_url,
                category=query,
                address=result["formatted_address"],
                RestaurantId=place_id,
            )
            print(restaurant_details)
            restaurant_details.save()

        pinned = False
        user_reviewed = False
        if request.user.is_authenticated:
            user_review = Review.objects.filter(restaurant=restaurant_details,
                                                user=user)
            profile = Profile.objects.get(user=user)
            if user_review.exists():
                user_reviewed = True
            if (
                profile.pinned_restaurants
                .filter(RestaurantId=place_id)
                .exists()
            ):
                pinned = True

        restaurant_results.append({
            "name": result["name"],
            "address": result["formatted_address"],
            "category": query,
            "image_urls": image_urls,
            "pinned": pinned,
            "user_reviewed": user_reviewed,
            "website_url": website_url,
            "place_id": place_id,
        })

    return render(request, 'home/results.html', {
        "restaurant_results": restaurant_results,
        "page_object": page_object,
        "restaurant_details": restaurant_details,
        "query": query,
        })


def home(request):
    """
    View to render homepage.
    """
    return render(request, 'home/index.html')
