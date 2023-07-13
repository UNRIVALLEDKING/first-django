from django.urls import path
from . import views

# from .views import api_home

# Define the URL patterns for your Django app

# The empty string "" represents the root URL of your app
# When a request is made to the root URL, it will be handled by the api_home view function from views.py
urlpatterns = [
    path("", views.api_home),
]
