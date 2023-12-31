# Generated by Django 3.2.20 on 2023-07-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True)),
                ('address', models.TextField()),
                ('RestaurantId', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
    ]
