# Catalyst Count

Catalyst Count is a web application built using Django that enables users to upload CSV files, filter data, and count records based on applied filters. The application supports user authentication and provides a user-friendly interface for data management and querying.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Overview](#project-overview)
- [Implementation Details](#implementation-details)
  - [Project Setup](#project-setup)
  - [Database Configuration](#database-configuration)
  - [User Authentication](#user-authentication)
  - [File Upload and Processing](#file-upload-and-processing)
  - [Data Filtering and Querying](#data-filtering-and-querying)
  - [User Interface](#user-interface)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [License](#license)

## Features
- User registration, login, and logout functionality.
- Upload CSV files up to 1GB with progress feedback.
- Filter data using various criteria through a query builder.
- View the count of records matching the applied filters.
- Asynchronous file processing to enhance performance.

## Technologies Used
- **Framework:** Django
- **Database:** PostgreSQL
- **Frontend:** Bootstrap 4, Django Template Engine
- **Background Task Processing:** Celery
- **APIs:** Django REST Framework (DRF)
- **Version Control:** Git
- **Environment Management:** django-environ

## Project Overview
The **catalyst-count** application aims to simplify the process of data management and querying for users who frequently work with large datasets stored in CSV files. The system is designed to handle significant data loads efficiently while providing a responsive and user-friendly interface.

## Implementation Details

### Project Setup
1. **Creating the Project:**
   - I began by setting up a new Django project named `catalyst-count` using the following command:
     ```bash
     django-admin startproject catalyst_count
     cd catalyst_count
     ```

2. **Setting Up the Virtual Environment:**
   - A virtual environment was created to manage the project dependencies effectively:
     ```bash
     python -m venv env
     source env/bin/activate  # On macOS/Linux
     .\env\Scripts\activate   # On Windows
     ```

3. **Installing Required Packages:**
   - I installed Django, PostgreSQL, Django REST Framework, Celery, and other necessary packages using:
     ```bash
     pip install django djangorestframework psycopg2-binary django-environ celery
     ```

### Database Configuration
1. **PostgreSQL Setup:**
   - I set up a PostgreSQL database called `catalyst_count`:
     ```sql
     CREATE DATABASE catalyst_count;
     added column names as CSV file 
     ```

2. **Model Creation:**
   - I created a model to handle the uploaded CSV data, `CompanyCSVData`, which corresponds to the structure of the dataset. This model includes fields such as company name, employee count, and other relevant attributes.
   
   ```python
   from django.db import models


class CompanyCSVData(models.Model):
    id = models.IntegerField(primary_key=True)  # Keep this if you want to manage IDs manually
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    size_range = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    current_employee_estimate = models.IntegerField(blank=True, null=True)
    total_employee_estimate = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'company_csv_data'  # Name of the table

    def __str__(self):
        return self.name


class CompanyCSVData(models.Model):
    id = models.IntegerField(primary_key=True)  # Keep this if you want to manage IDs manually
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    size_range = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    current_employee_estimate = models.IntegerField(blank=True, null=True)
    total_employee_estimate = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'company_csv_data'  # Name of the table

    def __str__(self):
        return self.name
