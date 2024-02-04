from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Patient, Counsellor, Appointment
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import status

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    def create(self, validated_data):
        email = validated_data.get('email')
        existing_patient = Patient.objects.filter(email=email)
        if Patient.objects.filter(email=email).exists():
            return self.update(existing_patient , validated_data)
        
        password = validated_data.get('password')
        validate_password(password)
        patient_instance = Patient.objects.create(**validated_data)
        return  patient_instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        password = validated_data.get('password',instance.password)
        if password:
            validate_password(password)
            instance.password=password


        instance.save()

        return instance

class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = '__all__'
    def create(self, validated_data):
        email = validated_data.get('email')
        existing_counsellor = Counsellor.objects.filter(email=email)
        if existing_counsellor:
            return self.update(existing_counsellor , validated_data)
        password = validated_data.get('password')
        validate_password(password)
        counsellor_instance = Counsellor.objects.create(**validated_data)
        return  counsellor_instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        password = validated_data.get('password',instance.password)
        if password:
            validate_password(password)
            instance.password=password

        instance.save()
        return instance
    

class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.filter(is_active=True))
    counsellor = serializers.PrimaryKeyRelatedField(queryset=Counsellor.objects.filter(is_active=True)) 
    appointment_date = serializers.DateTimeField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self,validated_data):        
        appointment_date = validated_data.get('appointment_date')
        patient = validated_data.get('patient')
        counsellor = validated_data.get('counsellor')

        if Appointment.objects.filter(patient=patient, counsellor=counsellor, appointment_date=appointment_date, is_active=True).exists():
            raise serializers.ValidationError("Duplicate appointment. Please choose a different date or time.")

        if appointment_date and appointment_date < timezone.now():
            raise serializers.ValidationError("Appointment date must be in the future.")
        return validated_data
