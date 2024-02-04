from django.contrib import admin

from .models import Patient, Counsellor, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'is_active']
    search_fields = ['id', 'name', 'email']
    list_filter = ['is_active']

@admin.register(Counsellor)
class CounsellorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'is_active']
    search_fields = ['id', 'name', 'email']
    list_filter = ['is_active']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'counsellor', 'appointment_date', 'is_active']
    search_fields = ['id', 'patient__name', 'counsellor__name', 'appointment_date']
    list_filter = ['is_active']
    date_hierarchy = 'appointment_date'