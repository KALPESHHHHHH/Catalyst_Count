from .models import UploadedFile
from django import forms

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
class CompanyFilterForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    domain = forms.CharField(max_length=255, required=False)
    year_founded = forms.IntegerField(required=False)
    industry = forms.CharField(max_length=255, required=False)
    size_range = forms.CharField(max_length=255, required=False)
    locality = forms.CharField(max_length=255, required=False)
    country = forms.CharField(max_length=255, required=False)