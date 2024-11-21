from django.contrib import admin
from .models import PatientsLogin, DoctorsLogin

class PatientsLoginAdmin(admin.ModelAdmin):
    list_display =['username', 'password']
admin.site.register(PatientsLogin,PatientsLoginAdmin)

class DoctorsLoginAdmin(admin.ModelAdmin):
    list_display =['username', 'password']
    admin.site.register(DoctorsLogin,PatientsLoginAdmin)
