from django.db import models


class Recipient(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class EmailCompany(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),

    ]

    title = models.CharField(max_length=100, help_text="Enter the message title ")
    message = models.TextField(help_text="Enter the text of the message ")
    recipients = models.ManyToManyField(Recipient, related_name='emails', help_text="Choose recipients")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


