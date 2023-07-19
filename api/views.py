from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Patient, Doctor, Appointment, CustomUser
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, CustomUserSerializer
from django.http import HttpResponse

# Create your views here.
@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def patient_detail(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patient, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def patient_create(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def patient_update(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def patient_delete(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response('Patient deleted')

@api_view(['GET'])
def doctor_list(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def doctor_detail(request, pk):
    doctor = Doctor.objects.get(id=pk)
    serializer = DoctorSerializer(doctor, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def doctor_create(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def doctor_update(request, pk):
    doctor = Doctor.objects.get(id=pk)
    serializer = DoctorSerializer(instance=doctor, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def doctor_delete(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return Response('Doctor deleted')

@api_view(['GET'])
def appointment_list(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointment_detail(request, pk):
    appointment = Appointment.objects.get(id=pk)
    serializer = AppointmentSerializer(appointment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def appointment_create(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def appointment_update(request, pk):
    appointment = Appointment.objects.get(id=pk)
    serializer = AppointmentSerializer(instance=appointment, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def appointment_delete(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return Response('Appointment deleted')


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")
