from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'catalyst'


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
        db_table = 'company_csv_data'  # Name of the tablecls

    def __str__(self):
        return self.name
