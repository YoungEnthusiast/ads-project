from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Person(AbstractUser):
    TYPE_CHOICES = [
        ('Poster', 'Poster'),
		('Admin', 'Admin'),
        ('SuperAdmin', 'SuperAdmin'),
    ]

    username = models.EmailField(max_length=60, unique=True, null=True, blank=True, verbose_name="Email")

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Poster', blank=True, null=True)

    country = models.CharField(max_length=30, null=True)

    paypal = models.EmailField(max_length=60, unique=True, null=True, blank=True, verbose_name="Paypal Email")
    bank_name = models.CharField(max_length=60, null=True, blank=True, verbose_name="Bank Name")
    account_no = models.CharField(max_length=15, null=True, blank=True, verbose_name="Account Number")
    account_name = models.CharField(max_length=45, null=True, blank=True, verbose_name="Account Name")
    referrer = models.CharField(max_length=60, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        # verbose_name = "Researcher's Profile"
        # verbose_name_plural = "Researcher's Profiles"

    def __str__(self):
        try:
            return str(self.username) + " - " + str(self.first_name) + " " + str(self.last_name)
        except:
            return str(self.id)
