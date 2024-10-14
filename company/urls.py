from django.urls import path
from . import views
from .views import (
    upload_data,
    filter_companies,
    users,
    add_user,
    remove_user,
    CompanyListCreateView  # Import the API view
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  # Updated to use user_login
    path('logout/', views.logout_page, name='logout'),
    path('navbar/', views.navbar, name='navbar'),
    path('users/', views.users, name='users'),
    path('add-user/', add_user, name='add_user'),
    path('remove-user/', remove_user, name='remove_user'),
    path('filter/', filter_companies, name='filter_companies'),
    path('upload_file/', upload_data, name='upload_data'),  # Updated to use upload_data
    path('api/companies/', CompanyListCreateView.as_view(), name='company-list-create'),  # New API endpoint
]
