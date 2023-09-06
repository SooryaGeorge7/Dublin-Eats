from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True,max_length=500)
    address = models.TextField()
    category = models.TextField(default="")
    RestaurantId = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name
