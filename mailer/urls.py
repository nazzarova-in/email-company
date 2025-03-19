from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmailCompanyViewSet

router = DefaultRouter()
router.register(r'email_companies', EmailCompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
