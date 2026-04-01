from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # Pacientes
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
    # Doctores
    path('doctores/', views.listar_doctores, name='listar_doctores'),
    path('doctores/nuevo/', views.crear_doctor, name='crear_doctor'),
    path('doctores/editar/<int:id>/', views.editar_doctor, name='editar_doctor'),
    path('doctores/eliminar/<int:id>/', views.eliminar_doctor, name='eliminar_doctor'),
    # Horas
    path('horas/', views.listar_horas, name='listar_horas'),
    path('horas/nueva/', views.crear_hora, name='crear_hora'),
    path('horas/editar/<int:id>/', views.editar_hora, name='editar_hora'),
    path('horas/eliminar/<int:id>/', views.eliminar_hora, name='eliminar_hora'),
]