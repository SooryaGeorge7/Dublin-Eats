# Generated by Django 3.2.20 on 2023-08-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_category'),
        ('users', '0002_profile_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pinned_restaurants',
            field=models.ManyToManyField(blank=True, related_name='to_visit', to='restaurants.Restaurant'),
        ),
    ]