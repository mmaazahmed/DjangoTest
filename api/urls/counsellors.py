from django.urls import path
from ..views.counsellor import counsellors,delete_counsellor,update_counsellor,create_counsellor,fetch_counsellor_by_email
urlpatterns = [
    path('', counsellors, name="list_counsellors"),
    path('delete/<int:counsellor_id>', delete_counsellor, name='delete_counsellor'),
    path('create/', create_counsellor, name='create_counsellor'),
    path('update/<int:counsellor_id>/', update_counsellor, name='update_counsellor'),
    path('fetch-email/<str:counsellor_email>/', fetch_counsellor_by_email, name='FetchCounsellorByEmail'),
]   