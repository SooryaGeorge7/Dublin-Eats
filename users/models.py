from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from restaurants.models import Restaurant
from django.core.validators import MaxLengthValidator


placeholder = (
    f"https://res.cloudinary.com/dif9bjzee/image/upload"
    f"/ar_1:1,b_rgb:262c35,bo_5px_solid_rgb:2c3e50,c_fill,g_auto,"
    f"r_max,w_200/v1689590568/profile-gda8c660e4_640_z54qoi.webp"
)


class Profile(models.Model):
    """
    Model for creating a profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(
        max_length=50, null=True, blank=True,
    )
    surname = models.CharField(
        max_length=50, null=True, blank=True,
    )
    about = models.TextField(
        null=True,
        blank=True,
        max_length=200,
        validators=[MaxLengthValidator(250)],
    )

    profile_image = CloudinaryField(
        "image",
        default=placeholder,
        eager=[{"width": 50, "height": 50, "crop": "crop"}],
        transformation={
            "width": 200,
            "height": 200,
            "crop": "fill",
        },
        blank=True,
        null=True,
    )
    fav_food = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[MaxLengthValidator(100)],
    )
    pinned_restaurants = models.ManyToManyField(
        Restaurant, related_name="to_visit", blank=True
    )
    reviewed = models.ManyToManyField(
        Restaurant, related_name="reviewed", blank=True
    )

    def __str__(self):
        """
        Returns the username of the profile as a string representation of
        the object.
        """
        return f'{self.user.username} Profile'
