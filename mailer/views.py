from rest_framework import viewsets

from .models import EmailCompany
from .serializers import EmailCompanySerializer


class EmailCompanyViewSet(viewsets.ModelViewSet):
    queryset = EmailCompany.objects.prefetch_related('recipients').all()
    serializer_class = EmailCompanySerializer


