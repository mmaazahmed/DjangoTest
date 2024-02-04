from django.urls import path
# from ..views.counsellor import counsellors,delete_counsellor,update_counsellor,create_counsellor,fetch_counsellor_by_email
from ..views.appointment import (
    appointments,
    delete_appointment,
    create_appointment,
    update_appointment,
    fetch_appointment,
    fetch_appointments_for_patient,
    fetch_appointments_for_counsellor,
    fetch_active_appointments_between_range,
)

urlpatterns = [
    path('', appointments, name="list_appointments"),
    path('delete/<int:appointment_id>', delete_appointment, name='delete_appointment'),
    path('create/', create_appointment, name='create_appointment'),
    path('update/<int:appointment_id>/', update_appointment, name='update_appointment'),
    path('fetch/', fetch_appointment, name='fetch_appointment'),
    path('for-patient/<int:patient_id>/', fetch_appointments_for_patient, name='fetch_appointments_for_patient'),
    path('for-counsellor/<int:counsellor_id>/', fetch_appointments_for_counsellor, name='fetch_appointments_for_counsellor'),
    path('active/', fetch_active_appointments_between_range, name='fetch_active_appointments_between_range'),
]   