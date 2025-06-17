from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email_verified = models.BooleanField(default=False, verbose_name="Email Verified")
    is_kyc_approved = models.BooleanField(default=False, verbose_name="KYC Approved")
    kyc_document = models.FileField(
        upload_to='kyc_documents/',
        null=True,
        blank=True,
        verbose_name="KYC Document"
    )