from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Patient, Counsellor, Appointment
from ..serializers import CounsellorSerializer

@api_view(['GET'])
def counsellors(request):

    queryset = Counsellor.objects.all()
    serializer = CounsellorSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_counsellor(request, counsellor_id):
    counsellor = get_object_or_404(Counsellor, id=counsellor_id)
    counsellor.soft_delete()
    return Response({'message': 'Counsellor soft-deleted successfully'})

@api_view(['POST'])
def create_counsellor(request):
    serializer = CounsellorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_counsellor(request, counsellor_id):
    counsellor = get_object_or_404(Counsellor, id=counsellor_id)
    serializer = CounsellorSerializer(counsellor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def fetch_counsellor_by_email(request, counsellor_email):
    counsellor = get_object_or_404(Counsellor, email=counsellor_email)
    serializer = CounsellorSerializer(counsellor)
    return Response(serializer.data)