from rest_framework import serializers
from .models import Patient,Doctor


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'


class DoctorSerializer(serializers.Serializer):
    fio=serializers.CharField()
    experience=serializers.IntegerField()

    def create(self, validated_data):
        return Doctor.objects.create(fio=validated_data['fio'],
                                     experience=validated_data['experience'])

    def update(self, instance, validated_data):
        instance.fio=validated_data['fio']
        instance.experience=validated_data['experience']
        return instance
