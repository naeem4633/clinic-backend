from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/admin', admin.site.urls),

    path('patient-list', views.patient_list),
    path('patient-detail', views.patient_detail),
    path('patient-create', views.patient_create),
    path('patient-update', views.patient_update),
    path('patient-delete', views.patient_delete),

    path('doctor-list', views.doctor_list),
    path('doctor-detail', views.doctor_detail),
    path('doctor-create', views.doctor_create),
    path('doctor-update', views.doctor_update),
    path('doctor-delete', views.doctor_delete),

    path('appointment-list', views.appointment_list),
    path('appointment-detail', views.appointment_detail),
    path('appointment-create', views.appointment_create),
    path('appointment-update', views.appointment_update),
    path('appointment-delete', views.appointment_delete),
]
