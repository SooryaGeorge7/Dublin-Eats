from django.urls import path
from . import views

urlpatterns = [
    path(
        "review/<str:restaurant_id>/",
        views.review,
        name="review",
    ),
    path(
        "allreviews/<str:restaurant_id>/",
        views.allreviews,
        name="allreviews",
    ),
    path(
        "edit_review/<str:restaurant_id>/<int:review_id>/",
        views.edit_review,
        name="edit_review",
    ),
    path(
        "profile_reviews/<str:restaurant_id>/",
        views.profile_reviews,
        name="profile_reviews",
    ),
    
]