from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Patient, Counsellor, Appointment
from ..serializers import AppointmentSerializer
from rest_framework import status
from django.utils import timezone


@api_view(['GET'])
def fetch_active_appointments_between_range(request):
    start_date = request.query_params.get('start_date', '')
    end_date = request.query_params.get('end_date', '')
    start_date = timezone.datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else timezone.now().date()
    end_date = timezone.datetime.strptime(end_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59) if end_date else timezone.now()
    end_date = end_date.date() if isinstance(end_date, timezone.datetime) else end_date
    appointments = Appointment.objects.filter(
        appointment_date__range=[start_date, end_date],
        is_active=True
    ).order_by('-appointment_date__day', '-appointment_date__month', '-appointment_date__year')
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetch_appointments_for_patient(request, patient_id):
    patient = get_object_or_404(Patient,id=patient_id)
    appointments = Appointment.objects.filter(patient=patient)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetch_appointments_for_counsellor(request, counsellor_id):
    counsellor = get_object_or_404(Counsellor, id=counsellor_id)
    appointments = Appointment.objects.filter(counsellor=counsellor)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def appointments(request):

    queryset = Appointment.objects.all()
    serializer = AppointmentSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['DELETE','GET'])
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.soft_delete()
    return Response({'message': 'Appointment soft-deleted successfully'})

@api_view(['POST'])
def create_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def update_appointment(request, appointment_id):
    appointment_instance = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'PUT':
        serializer = AppointmentSerializer(appointment_instance, data=request.data)
    elif request.method == 'PATCH':
        serializer = AppointmentSerializer(appointment_instance, data=request.data, partial=True)   

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def fetch_appointment(request):
    try:
        patient_id = int(patient_id)
        counsellor_id = int(counsellor_id)
        appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
    except (ValueError, TypeError) as e:
        return Response({"error": f"Invalid parameter values: {e}"}, status=400)

    patient = get_object_or_404(Patient, id=patient_id, is_active=True)
    counsellor = get_object_or_404(Counsellor, id=counsellor_id, is_active=True)

    appointment = get_object_or_404(
        Appointment,
        patient=patient,
        counsellor=counsellor,
        appointment_date=appointment_date,
        is_active=True
    )

    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)