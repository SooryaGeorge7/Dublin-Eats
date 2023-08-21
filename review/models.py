from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from django.core.validators import MaxLengthValidator


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    Rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    taste = models.IntegerField(choices=Rating, default=0)
    ambience = models.IntegerField(choices=Rating, default=0)
    customer_service = models.IntegerField(choices=Rating, default=0)
    location = models.IntegerField(choices=Rating, default=0)
    value_for_money = models.IntegerField(choices=Rating, default=0)
    comment_text = models.TextField(null=True,
        blank=True,
        validators=[MaxLengthValidator(500)],
        )

    class Meta:

        ordering = ["-created_on"]


    def __str__(self):
        return f"{self.user.username}'s review of {self.restaurant.name}"