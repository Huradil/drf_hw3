from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


