from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Patient, Counsellor, Appointment
from ..serializers import PatientSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls={
        'pokemon',
    }
    return Response(api_urls)

@api_view(['GET'])
def patients(request):
    queryset = Patient.objects.all()
    serializer = PatientSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    # fetch_patient(request,patient_id)
    patient.soft_delete()
    return Response({'message': 'Patient soft-deleted successfully'})

@api_view(['GET'])
def fetch_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)

@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    serializer = PatientSerializer(patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def fetch_patient_by_email(request, patient_email):
    patient = get_object_or_404(Patient, email=patient_email)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)
