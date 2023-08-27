from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestViews(TestCase):
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
