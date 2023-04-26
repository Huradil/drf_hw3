from django.urls import path
from . import views

urlpatterns=[
    path('doctors/',views.doctor_list_crate_api_view),
    path('patient/',views.PatientListCreateAPIView.as_view()),
]
