from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewCreateView.as_view(), name="create-review"),
    path("thank-you/", views.ThankYouView.as_view(), name="thank-you"),
    path("all-reviews/", views.ReviewsListView.as_view(), name="review-list"),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="single-review"),
]
