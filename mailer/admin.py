from django.contrib import admin
from .models import EmailCompany, Recipient

admin.site.register(EmailCompany)
admin.site.register(Recipient)
