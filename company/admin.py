from django.contrib import admin

from .models import CompanyCSVData


@admin.register(CompanyCSVData)
class CompanyCSVDataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'domain', 
        'year_founded', 
        'industry', 
        'size_range', 
        'locality', 
        'country', 
        'linkedin_url', 
        'current_employee_estimate', 
        'total_employee_estimate'
    )
