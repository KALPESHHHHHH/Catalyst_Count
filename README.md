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
## Model Creation

In the Company Count application, a model named `CompanyCSVData` was created to handle the uploaded CSV data. This model corresponds to the structure of the dataset and includes fields that represent relevant attributes of the company data.

### CompanyCSVData Model

The `CompanyCSVData` model includes the following fields:

- **id**: IntegerField (primary key) - A unique identifier for each record. This is kept to manage IDs manually.
- **name**: CharField - The name of the company.
- **domain**: CharField (optional) - The company's website domain.
- **year_founded**: IntegerField (optional) - The year the company was founded.
- **industry**: CharField (optional) - The industry in which the company operates.
- **size_range**: CharField (optional) - The size range of the company.
- **locality**: CharField (optional) - The locality of the company.
- **country**: CharField (optional) - The country where the company is located.
- **linkedin_url**: URLField (optional) - A link to the company’s LinkedIn profile.
- **current_employee_estimate**: IntegerField (optional) - An estimate of the current number of employees.
- **total_employee_estimate**: IntegerField (optional) - An estimate of the total number of employees.

Here is the implementation of the `CompanyCSVData` model:

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
## Database Migrations (Windows)

Django uses migrations to manage database schema changes. This section outlines how to create, apply, and manage migrations in the Company Count Application on a Windows environment.

### Creating Migrations

Whenever you make changes to your models (e.g., adding a field, changing a data type, etc.), you need to create a migration to reflect those changes in the database. To create migrations, run the following commands in your terminal (Command Prompt or PowerShell):

python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
## Docker Setup

This section provides instructions for building and running the Docker image for the Company Count Application. Docker allows you to package your application with all its dependencies, ensuring consistent environments across different machines.

### Prerequisites

Before proceeding, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop) (make sure Docker Desktop is running)
- [Docker Compose](https://docs.docker.com/compose/)

### Building the Docker Image

1. **Navigate to the Project Directory**:  
   Open your terminal (Command Prompt or PowerShell) and navigate to the root directory of your Django project:

   ```bash
   cd C:\Projects\Ennobridge\Count_App\catalyst_count
