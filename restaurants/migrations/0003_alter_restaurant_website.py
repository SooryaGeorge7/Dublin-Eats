# Generated by Django 3.2.20 on 2023-09-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='website',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
