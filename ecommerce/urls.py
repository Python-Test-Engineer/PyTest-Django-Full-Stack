from ecommerce import views
from django.urls import path

urlpatterns = [
    path("", views.CategoryCreateView.as_view(), name="category-create"),
]
