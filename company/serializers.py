from rest_framework import serializers
from .models import CompanyCSVData

class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCSVData
        fields = '__all__'  # Include all fields in the serializer
