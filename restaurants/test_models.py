from django.test import TestCase
from django.contrib.auth.models import User
from .models import Restaurant


class TestRestaurantModel(TestCase):
    def setUp(self):
        Restaurant.objects.create(
            name="Test Restaurant",
            website="dublineatstest@info.com",
            address="07 Tester, Dublin",
            category="indian",
            RestaurantId="test17",
        )

    def test_restaurant_model(self):
        """
        This unit test case is verifying that the "Restaurant" model
        behaves as expected and checks if the attributes of that instance match 
        the expected values.
        """
        restaurant = Restaurant.objects.get(name="Test Restaurant")
        self.assertEqual(restaurant.name, "Test Restaurant")
        self.assertEqual(restaurant.website, "dublineatstest@info.com")
        self.assertEqual(restaurant.address, "07 Tester, Dublin")
        self.assertEqual(restaurant.category, "indian")
        self.assertEqual(restaurant.RestaurantId, "test17")
