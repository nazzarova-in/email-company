from rest_framework import serializers
from .models import Recipient, EmailCompany


class RecipientSerializer(serializers.ModelSerializer):
    emails = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipient
        fields = ["id", "email"]


class EmailCompanySerializer(serializers.ModelSerializer):
    recipients = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipient.objects.all())

    class Meta:
        model = EmailCompany
        fields = ["id", "title", "message", "recipients", "status"]

    def validate_recipients(self, value):
        if not value:
            raise serializers.ValidationError("At least one recipient is required.")

        email_list = [recipient.email for recipient in value]

        if len(email_list) != len(set(email_list)):
            raise serializers.ValidationError(("Recipients' emails must be unique."))

        return value




