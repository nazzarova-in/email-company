from django.db import models
from django.core.mail import send_mail
from django.utils.timezone import now


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
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def send_emails(self):
        recipient_emails = [recipient.email for recipient in self.recipients.all()]

        if not recipient_emails:
            return "No recipients to send emails to."

        send_mail(
            subject=self.title,
            message=self.message,
            from_email="nazzarova.in@gmail.com",
            recipient_list=recipient_emails,
            fail_silently=False,
        )

        self.status = 'sent'
        self.sent_at = now()
        self.save()

        return f"Emails sent to {len(recipient_emails)} recipients."




