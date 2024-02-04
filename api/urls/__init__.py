from django.urls import path, include
from ..views.patient import api_overview

urlpatterns = [
    path('', api_overview, name="api_overview"),
    path('patients/', include('api.urls.patients')),
    path('counsellors/', include('api.urls.counsellors')),
    path('appointments/', include('api.urls.appointments')),

]