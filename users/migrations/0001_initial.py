# Generated by Django 3.2.20 on 2023-07-23 08:50

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, default='Firstname', max_length=50, null=True)),
                ('surname', models.CharField(blank=True, default='Surname', max_length=50, null=True)),
                ('about', models.TextField(blank=True, default='Foodie in and out..!', max_length=200, null=True)),
                ('profile_image', cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dif9bjzee/image/upload/c_scale,h_50,w_50/v1689590568/profile-gda8c660e4_640_z54qoi.webp', max_length=255, null=True, verbose_name='image')),
                ('fav_food', models.CharField(blank=True, default="What's your favourite cuizine?", max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
