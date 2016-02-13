from django.contrib import admin
from .models import Patient, User_Credential

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'phone', 'birthday', 'sent')

admin.site.register(Patient, PatientAdmin)

class User_CredentialAdmin(admin.ModelAdmin):
	list_display = ('access_token', 'refresh_token', 'expiry_time')

admin.site.register(User_Credential, User_CredentialAdmin)
