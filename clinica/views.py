from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente, Doctor, HoraMedica
from .forms import PacienteForm, DoctorForm, HoraMedicaForm

# Dashboard principal
@login_required
def dashboard(request):
    return render(request, 'clinica/dashboard.html', {
        'pacientes': Paciente.objects.count(),
        'doctores': Doctor.objects.count(),
        'horas': HoraMedica.objects.count(),
        'usuario': request.user.username,
    })

# ---- PACIENTES ----
@login_required
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/pacientes/lista.html', {'pacientes': pacientes})

@login_required
def crear_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')
    return render(request, 'clinica/pacientes/form.html', {'form': form, 'titulo': 'Nuevo Paciente'})

@login_required
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')
    return render(request, 'clinica/pacientes/form.html', {'form': form, 'titulo': 'Editar Paciente'})

@login_required
def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'clinica/confirmar_eliminar.html', {
        'objeto': paciente,
        'cancelar_url': '/pacientes/',
    })

# ---- DOCTORES ----
@login_required
def listar_doctores(request):
    doctores = Doctor.objects.all()
    return render(request, 'clinica/doctores/lista.html', {'doctores': doctores})

@login_required
def crear_doctor(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_doctores')
    return render(request, 'clinica/doctores/form.html', {'form': form, 'titulo': 'Nuevo Doctor'})

@login_required
def editar_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('listar_doctores')
    return render(request, 'clinica/doctores/form.html', {'form': form, 'titulo': 'Editar Doctor'})

@login_required
def eliminar_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('listar_doctores')
    return render(request, 'clinica/confirmar_eliminar.html', {
        'objeto': doctor,
        'cancelar_url': '/doctores/',
    })

# ---- HORAS MÉDICAS ----
@login_required
def listar_horas(request):
    horas = HoraMedica.objects.all()
    return render(request, 'clinica/horas/lista.html', {'horas': horas})

@login_required
def crear_hora(request):
    form = HoraMedicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_horas')
    return render(request, 'clinica/horas/form.html', {'form': form, 'titulo': 'Nueva Hora Médica'})

@login_required
def editar_hora(request, id):
    hora = get_object_or_404(HoraMedica, id=id)
    form = HoraMedicaForm(request.POST or None, instance=hora)
    if form.is_valid():
        form.save()
        return redirect('listar_horas')
    return render(request, 'clinica/horas/form.html', {'form': form, 'titulo': 'Editar Hora Médica'})

@login_required
def eliminar_hora(request, id):
    hora = get_object_or_404(HoraMedica, id=id)
    if request.method == 'POST':
        hora.delete()
        return redirect('listar_horas')
    return render(request, 'clinica/confirmar_eliminar.html', {
        'objeto': hora,
        'cancelar_url': '/horas/',
    })