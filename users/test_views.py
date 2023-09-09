from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestViews(TestCase):
    """
    This test cases ensure that the views related to user profiles, including viewing, 
    editing, and deleting profile.It tests that site logs in the test user using the client,
     then It sends a GET request to a URL named "profile" with the test user's username as
    a parameter.It checks  if the "profile.html" template is used.When user wants to edit
    a profile,the site sends a POST request to a URL named "editprofile" with the test user's
    username as an argument and data for updating the user's first and last name.It checks if
     the "edit_profile.html" template is used.When user wants to delete their profile, 
     the site sends a POST request to a URL named "deleteprofile" with the test user's 
     username as an argument.It checks if redirected URL is the home page.
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="testpassword"
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse(
            "profile",
            kwargs={"username": "testuser"}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile.html")

    def test_edit_profile_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse(
            "editprofile", args=[self.user.username]
            ), data={
            "first_name": "Updated Firstname",
            "last_name": "Updated Lastname",
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/edit_profile.html")

    def test_delete_profile_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse(
            "deleteprofile",
            args=[self.user.username]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("dublineats-home"))
