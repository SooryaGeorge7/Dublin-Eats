# Generated by Django 3.2.20 on 2023-08-21 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230819_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, default='Please update about info', max_length=200, null=True, validators=[django.core.validators.MaxLengthValidator(250)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fav_food',
            field=models.CharField(blank=True, default='Please update info', max_length=50, null=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, default='Please update name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, default='surname', max_length=50, null=True),
        ),
    ]
