from django.db import models
from django.urls import reverse
from django.db.models import Sum, Count
from django_countries.fields import CountryField

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    profile_picture = models.FileField(upload_to='uploads/', blank=True)
    phone_number = models.CharField(max_length=255, blank=False)
    email_address = models.CharField(max_length=255, default='email@domain.com')
    postal_address = models.TextField(default='Postal address')
    country = CountryField() #models.CharField(max_length=255)

    def __str__(self):
        return self.last_name + ', ' + self.first_name

    def get_absolute_edit(self):
        return reverse('edit_contact', args=[str(self.id)])
