from django.urls import path
from ..views.patient import patients, fetch_patient, create_patient,api_overview,fetch_patient_by_email,update_patient,delete_patient 
urlpatterns = [
    path('', patients, name="list_patients"),
    path('create/', create_patient, name='create_patient'),
    path('update/<int:patient_id>/', update_patient, name='update_patient'),
    path('delete/<int:patient_id>', delete_patient, name='delete_patient'),
    path('fetch-id/<int:patient_id>/', fetch_patient, name='FetchPatientById'),
    path('fetch-email/<str:patient_email>/', fetch_patient_by_email, name='FetchPatientByEmail'),
]   