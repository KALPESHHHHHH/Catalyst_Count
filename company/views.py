from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UploadFileForm
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import CompanyCSVData
from django.views.decorators.csrf import csrf_exempt  
from .serializers import CompanyDataSerializer
from django.contrib import messages
from django.views import View
from io import StringIO
from allauth.account.views import PasswordResetView
from .tasks import process_csv
from .forms import CompanyFilterForm 
from django.db import IntegrityError
import logging
from django.db.models import Q
import csv
from rest_framework import generics
from .serializers import CompanyDataSerializer
import pandas as pd
import io
from celery import shared_task  # Assuming Celery is used for background processing
from smtplib import SMTPAuthenticationError
import os

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('account_login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('query_builder')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'account/login.html')

# Logout view
@login_required
def logout_page(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('account_login')

# Navbar page
@login_required
def navbar(request):
    return render(request, 'navbar.html')

# Users list
@login_required
def users(request):
    users = User.objects.all()
    message = request.GET.get('message', '')
    return render(request, 'users.html', {'users': users, 'message': message})

# Add user view with CSRF protection
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        is_active = request.POST.get('is_active') == 'True'

        # Create new user
        user = User.objects.create_user(username=username, email=email)
        user.is_active = is_active
        user.save()

        return JsonResponse({
            'message': 'User added successfully!',
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active
        })
    return JsonResponse({'message': 'Invalid request'}, status=400)

# Remove user view with CSRF protection
def remove_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.delete()  # This will remove the user from the database
            return JsonResponse({'message': 'User removed successfully!'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
    return JsonResponse({'message': 'Invalid request'}, status=400)

@login_required
def filter_companies(request):
    form = CompanyFilterForm(request.GET or None)
    companies = CompanyCSVData.objects.all()  # Get all companies initially
    filters = Q()  # Initialize an empty Q object for complex queries

    if form.is_valid():
        # Fetch cleaned data from the form
        name = form.cleaned_data.get('name')
        domain = form.cleaned_data.get('domain')
        year_founded = form.cleaned_data.get('year_founded')
        industry = form.cleaned_data.get('industry')
        size_range = form.cleaned_data.get('size_range')
        locality = form.cleaned_data.get('locality')
        country = form.cleaned_data.get('country')

        # Build the filters dynamically using exact matches
        if name:
            filters &= Q(name__exact=name)  # Use exact match
        if domain:
            filters &= Q(domain__exact=domain)  # Use exact match
        if year_founded is not None:
            filters &= Q(year_founded=year_founded)  # Match directly
        if industry:
            filters &= Q(industry__exact=industry)  # Use exact match
        if size_range:
            filters &= Q(size_range__exact=size_range)  # Use exact match
        if locality:
            filters &= Q(locality__exact=locality)  # Use exact match
        if country:
            filters &= Q(country__exact=country)  # Use exact match

        # Apply the filters to the queryset if any filters are set
        if filters:
            companies = companies.filter(filters)

    count = companies.count()  # Get the count of filtered companies

    # Get all records to display (optional)
    records = companies.values()  # Fetch all records

    return render(request, 'query_builder.html', {'form': form, 'count': count, 'records': records})
def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                decoded_file = uploaded_file.read().decode('utf-8')  # Decode the uploaded file
                io_string = io.StringIO(decoded_file)  # StringIO to treat string as file
                reader = csv.DictReader(io_string)  # CSV reader to read rows as dictionaries

                # Prepare a list to store the CompanyCSVData instances to be bulk created
                company_data_list = []

                for row in reader:
                    company_data_list.append(
                        CompanyCSVData(
                            id=row['id'],  # Explicitly handling the ID field
                            name=row['name'],
                            domain=row.get('domain', ''),
                            year_founded=row.get('year_founded', None),
                            industry=row.get('industry', ''),
                            size_range=row.get('size_range', ''),
                            locality=row.get('locality', ''),
                            country=row.get('country', ''),
                            linkedin_url=row.get('linkedin_url', ''),
                            current_employee_estimate=row.get('current_employee_estimate', None),
                            total_employee_estimate=row.get('total_employee_estimate', None)
                        )
                    )

                # Use bulk_create to save all records at once for performance
                CompanyCSVData.objects.bulk_create(company_data_list)

                return JsonResponse({'message': 'File uploaded and data saved successfully!'})
            except Exception as e:
                return JsonResponse({'message': str(e)}, status=400)
    else:
        form = UploadFileForm()
    return render(request, 'upload_data.html', {'form': form})

from django.db.models import Q
from rest_framework import generics
from .models import CompanyCSVData
from .serializers import CompanyDataSerializer

# DRF API View for Company Data
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = CompanyCSVData.objects.all()
    serializer_class = CompanyDataSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Initialize an empty Q object for complex queries
        filters = Q()

        # Apply filtering based on request parameters
        name = self.request.query_params.get('name')
        domain = self.request.query_params.get('domain')
        year_founded = self.request.query_params.get('year_founded')
        industry = self.request.query_params.get('industry')
        size_range = self.request.query_params.get('size_range')
        locality = self.request.query_params.get('locality')
        country = self.request.query_params.get('country')

        # Build the filters dynamically
        if name:
            filters &= Q(name__exact=name)  # Use exact match
        if domain:
            filters &= Q(domain__exact=domain)  # Use exact match
        if year_founded:
            filters &= Q(year_founded=year_founded)  # Match directly
        if industry:
            filters &= Q(industry__exact=industry)  # Use exact match
        if size_range:
            filters &= Q(size_range__exact=size_range)  # Use exact match
        if locality:
            filters &= Q(locality__exact=locality)  # Use exact match
        if country:
            filters &= Q(country__exact=country)  # Use exact match

        # Apply the filters to the queryset
        if filters:
            queryset = queryset.filter(filters)

        return queryset
