# Generated by Django 3.2.20 on 2023-08-19 22:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_pinned_restaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, default='Foodie in and out..!', max_length=200, null=True, validators=[django.core.validators.MaxLengthValidator(250)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fav_food',
            field=models.CharField(blank=True, default="What's your favourite cuizine?", max_length=50, null=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
