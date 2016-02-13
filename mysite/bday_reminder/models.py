from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	email = models.TextField()
	phone = models.TextField()
	birthday = models.DateField(null=True, blank=True)
	sent = models.BooleanField(default=False)

class User_Credential(models.Model):
	access_token = models.TextField()
	refresh_token = models.TextField()
	expiry_time = models.DateTimeField(null=True, blank=True)
