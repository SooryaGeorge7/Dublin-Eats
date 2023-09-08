import os
from django.test import TestCase, Client
from django.urls import reverse
import requests
from django.contrib.auth.models import User
from users.models import Profile
from review.models import Review, Restaurant


GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")


class TestSearchResultsViews(TestCase):
    """
    This is the setup method that is executed before each test function within the test case.
    The test environment is prepared, including creating a test user,
    a test profile, a test restaurant, and a test review. The test user is logged in, 
    and the test restaurant is added to the user's pinned restaurants and reviewed restaurants.
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="testing@user.com", password="test123"
        )
        self.profile = Profile.objects.get(user=self.user)
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            website="Test website",
            address="test user address 07, Dublin",
            RestaurantId="c454h5",
        )
        self.review = Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
        )
        self.profile.pinned_restaurants.add(self.restaurant)
        self.profile.reviewed.add(self.restaurant)

    def test_search_and_search_results_page(self):
        """
        This test checks if the search and search results
        pages function correctly by logging in a test user, performing a 
        search, and verifying the expected HTTP responses and page templates.
        
        """
        self.client.login(username="testuser", password="test123")
        query = "thai"
        response = self.client.get(reverse("search") + "?query=" + query)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("searchresults", kwargs={"query": query})
        )
        response = self.client.get(
            reverse("searchresults", kwargs={"query": query})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/results.html")
