from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Doctor,Patient
from .serializers import DoctorSerializer,PatientSerializer
from .my_generic import MyGenericRetrieveUpdateDestroy


@api_view(http_method_names=['POST','GET'])
def doctor_list_crate_api_view(request):
    if request.method=='GET':
        doctors=Doctor.objects.all()
        serializer=DoctorSerializer(instance=doctors,many=True)
        return Response(serializer.data,status=200)

    if request.method=='POST':
        received_data=request.data
        serializer=DoctorSerializer(data=received_data)
        if serializer.is_valid():
            doctor=serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)


@api_view(http_method_names=['POST','GET'])
def patient_list_create_api_view(request):
    if request.method=='GET':
        patients=Patient.objects.all()
        serializer=PatientSerializer(instance=patients,many=True)
        return Response(serializer.data,status=200)
    if request.method=='POST':
        received_data=request.data
        serializer=PatientSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)


class PatientRetrieveUpdateDeleteView(MyGenericRetrieveUpdateDestroy):
    model = Patient
    serializer_class = PatientSerializer


class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer



