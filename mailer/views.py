from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import EmailCompany
from .serializers import EmailCompanySerializer


class EmailCompanyViewSet(viewsets.ModelViewSet):
    queryset = EmailCompany.objects.prefetch_related('recipients').all()
    serializer_class = EmailCompanySerializer

    @action(detail=True, methods=['post'])
    def send_company(self, request, pk=None):
        email_company = self.get_object()

        if email_company.recipients.exists() and email_company.status =="draft":
            email_company.send_emails()
            return Response({"message": "Emails sent!"})

        return Response({"error": "Cannot send emails!"}, status=400)





