from django.urls import path
from . import views

urlpatterns=[
    path('doctors/',views.doctor_list_crate_api_view),
    path('patient/',views.patient_list_create_api_view),
    path('patient/<int:pk>/',views.PatientRetrieveUpdateDeleteView.as_view()),
    path('doctor/<int:pk>/',views.DoctorRetrieveUpdateDestroyView.as_view()),
]
