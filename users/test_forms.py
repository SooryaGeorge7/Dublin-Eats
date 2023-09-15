from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserUpdateForm, ProfileUpdateForm


class UserUpdateFormTest(TestCase):
    """
    The unit tests ensures that the UserUpdateForm and ProfileUpdateForm 
    forms behave correctly in terms of validation. They cover scenarios
     involving valid data, invalid email formats, missing required fields,
      and fields exceeding character limits.
    """
    def test_userupdateform_valid(self):
        form_data = {
            "username": "testuser",
            "email": "test@example.com",

        }
        form = UserUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_userupdateform_invalid_email(self):
        form_data = {
            "username": "testuser",
            "email": "incorrectemail",
        }
        form = UserUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors.keys())
        self.assertEqual(
            form.errors["email"][0], "Enter a valid email address."
        )

    def test_userupdateform_missing_fields(self):
        form_data = {
            "username": "",
            "email": "test@example.com",
        }
        form = UserUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors.keys())
        self.assertEqual(
            form.errors["username"][0], "This field is required."
        )


class TestProfileForm(TestCase):
    def test_ifprofileform_valid(self):
        form_data = {
                "firstname": "soorya",
                "surname": "george",
                "about": "Foodie until i die",
                "profile_image": "image.jpg",
                "fav_food": "indian",
        }

        form = ProfileUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ifprofileform_invalid(self):
        form = ProfileUpdateForm(
            {
                "firstname": str("a" * 51),
                "surname": str("a" * 51),
                "about": str("a" * 201),
                "fav_food": str("a" * 51),
            }
        )
        self.assertIn("firstname", form.errors.keys())
        self.assertIn("surname", form.errors.keys())
        self.assertIn("about", form.errors.keys())
        self.assertIn("fav_food", form.errors.keys())
        self.assertEqual(
            form.errors["firstname"][0],
            'Ensure this value has at most 50 characters (it has 51).',
        )
        self.assertEqual(
            form.errors["surname"][0],
            'Ensure this value has at most 50 characters (it has 51).',
        )
        self.assertEqual(
            form.errors["about"][0],
            'Ensure this value has at most 200 characters (it has 201).',
        )
        self.assertEqual(
            form.errors["fav_food"][0],
            'Ensure this value has at most 50 characters (it has 51).',
        )

        self.assertFalse(form.is_valid())
