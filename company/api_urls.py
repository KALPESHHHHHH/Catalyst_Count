from django.urls import path
from .views import CompanyDataViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'company-data', CompanyDataViewSet)

urlpatterns = router.urls
