
import os
from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from .models import Restaurant


GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")

def get_place_details(place_id):
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
    if category == "asian":
        
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=Asian%20restaurants%20in%20Dublin&key={GOOGLE_PLACES_API_KEY}"
        )
            
    elif category == "european":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=European%20restaurants%20in%20Dublin&key={GOOGLE_PLACES_API_KEY}"
        )
    elif category == "african":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=African%20restaurants%20in%20Dublin&key={GOOGLE_PLACES_API_KEY}"
        )
    elif category == "irish":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=Irish%20restaurants%20in%20Dublin&key={GOOGLE_PLACES_API_KEY}"
        )
    elif category == "american":
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=American%20restaurants%20in%20Dublin&key={GOOGLE_PLACES_API_KEY}"
        )
    
    else:
        pass
    
    restaurants = []
    response = requests.get(url)
    restaurant_data = response.json()
    results = restaurant_data.get("results", [])
    
    for result in results:
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
                            image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={GOOGLE_PLACES_API_KEY}"
                            image_urls.append(image_url)
                else:
                    image_urls.append("https://res.cloudinary.com/dif9bjzee/image/upload/v1688163762/backgroud_hwsqzo.webp")

            else:
                website_url = ""

            try:
                restaurant_details = Restaurant.objects.get(RestaurantId=place_id)
            except Restaurant.DoesNotExist:
                restaurant_details = Restaurant(
                    name = result["name"],
                    website = website_url,
                    address = result["formatted_address"],
                    RestaurantId = place_id,
                )            
                print(restaurant_details)
                restaurant_details.save()
            
            restaurants.append({
                "name": result["name"],
                "address": result["formatted_address"],
                "image_urls" : image_urls,
                "website_url": website_url,
                "place_id": place_id,
            })

    return render(request, 'restaurants/categories.html', {
        "restaurants":restaurants,
        })