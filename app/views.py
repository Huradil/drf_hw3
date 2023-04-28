from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Doctor,Patient
from .serializers import DoctorSerializer,PatientSerializer


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


@api_view(http_method_names=['PUT','GET','DELETE'])
def patient_retrieve_update_destroy_api_view(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method=="GET":
        serializer=PatientSerializer(instance=patient)
        return Response(serializer.data)
    if request.method=="PUT":
        serializer=PatientSerializer(instance=patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    if request.method=="DELETE":
        patient.delete()
        return Response(status=204)

@api_view(http_method_names=['GET','PUT','DELETE'])
def doctor_retrieve_update_destroy_api_view(request,pk):
    doctor=get_object_or_404(Doctor,pk=pk)
    if request.method=='GET':
        serializer=DoctorSerializer(instance=doctor)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer=DoctorSerializer(instance=doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    if request.method=='DELETE':
        doctor.delete()
        return Response(status=204)





