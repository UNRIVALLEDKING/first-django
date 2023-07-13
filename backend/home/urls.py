# Import the admin module for Django's built-in admin interface
from django.contrib import admin

# Import the path and include functions from the django.urls module
from django.urls import path, include

# Define the URL patterns for your Django project

# The first URL pattern maps the /admin/ URL to the Django admin site
# This allows access to the built-in admin interface provided by Django
urlpatterns = [
    path("admin/", admin.site.urls),
    # The second URL pattern maps the /api/ URL to the included URLs from the api app
    # This allows routing to the URLs defined in the api app
    path("api/", include("api.urls")),
]
