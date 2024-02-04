from django.db import models
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Patient(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    is_active=models.BooleanField(default=True)

    objects = SoftDeleteManager()
    def soft_delete(self):
        self.is_active = False
        self.save()

class Counsellor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    objects = SoftDeleteManager()
    def soft_delete(self):
        self.is_active = False
        self.save()



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    counsellor = models.ForeignKey(Counsellor, on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    objects = SoftDeleteManager()
    def soft_delete(self):
     
        self.is_active = False
        self.save()