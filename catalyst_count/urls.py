from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from company.views import user_login  # Import the login view from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('company.urls')),  # Include the app's urls
    path('accounts/', include('allauth.urls')),  # For user authentication using django-allauth
    path('', user_login, name='login'),  # Redirect root to the login view
]
