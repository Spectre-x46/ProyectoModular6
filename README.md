# 🏥 VitalCare — Sistema de Gestión Médica

> **Proyecto de evaluación final — Módulo 6**
> Curso Full Stack Python | Kibernum IT Academy

---

## 📌 Sobre el Proyecto

VitalCare es una aplicación web para la gestión de una clínica médica, desarrollada como proyecto de evaluación del **Módulo 6** del curso Full Stack Python. El objetivo fue demostrar el dominio de los fundamentos de Python aplicados al desarrollo web con Django, integración con bases de datos relacionales y despliegue de una arquitectura MVC completa.

La clínica requería un sistema donde personas autenticadas puedan **registrar, consultar, modificar y eliminar** horas clínicas, pacientes y doctores.

![Dashboard VitalCare](file:///C:/Users/Neo/.gemini/antigravity/brain/dc39b06a-8fff-44e2-8a40-a7060c1a38d5/dashboard_view_1775016550335.png)

---

## 🎯 Competencias Demostradas

- ✅ Configuración de un proyecto Django desde cero
- ✅ Diseño y creación de base de datos relacional en **PostgreSQL**
- ✅ Modelado de entidades con relaciones (`ForeignKey`)
- ✅ Sistema de autenticación con sesiones (login / logout)
- ✅ Implementación del patrón **CRUD** completo para 3 modelos
- ✅ Diseño responsive con **Bootstrap 5**
- ✅ Buenas prácticas: variables de entorno (`.env`), `.gitignore`, separación de configuración
- ✅ Panel de administración Django Admin

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología |
|---|---|
| Backend | Python 3 + Django 6.0.3 |
| Base de datos | PostgreSQL |
| Frontend | Bootstrap 5.3 + HTML5 |
| Autenticación | Django Auth (sesiones) |
| Variables de entorno | python-dotenv |

---

## 📐 Modelos de Datos

```
Paciente          Doctor              HoraMedica
─────────         ──────────          ──────────────────
nombre            nombre              paciente → Paciente
apellido          apellido            doctor   → Doctor
edad              edad                fecha
fecha_nacimiento  fecha_nacimiento     hora
                  especialidad        motivo
```

---

## 🚀 Instalación y Uso

### Requisitos previos
- Python 3.x
- PostgreSQL con la base de datos `clinica` creada

### Pasos

```bash
# 1. Clonar el repositorio
git clone <url>
cd vitalcare

# 2. Activar entorno virtual e instalar dependencias
python -m venv venv
.\venv\Scripts\activate       # Windows
pip install -r requirements.txt

# 3. Configurar variables de entorno
copy .env.example .env
# Editar .env con tus credenciales de PostgreSQL

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear usuario administrador
python manage.py createsuperuser

# 6. Correr el servidor
python manage.py runserver
```

Abrir en el navegador → **http://127.0.0.1:8000/**

---

## 🗺️ Rutas del Sistema

| Ruta | Función |
|---|---|
| `/` | Redirige al login automáticamente |
| `/login/` | Inicio de sesión |
| `/dashboard/` | Panel principal con estadísticas |
| `/pacientes/` | Gestión de pacientes (CRUD) |
| `/doctores/` | Gestión de doctores (CRUD) |
| `/horas/` | Gestión de horas médicas (CRUD) |
| `/admin/` | Panel de administración Django |

---

## 📁 Estructura del Proyecto

```
vitalcare/
├── clinica/                     # App principal
│   ├── migrations/              # Migraciones de BD
│   ├── templates/clinica/       # Vistas HTML con Bootstrap
│   │   ├── base.html            # Layout base con navbar
│   │   ├── login.html           # Pantalla de login
│   │   ├── dashboard.html       # Panel de control
│   │   ├── confirmar_eliminar.html
│   │   ├── pacientes/           # Templates CRUD pacientes
│   │   ├── doctores/            # Templates CRUD doctores
│   │   └── horas/               # Templates CRUD horas
│   ├── models.py                # Modelos: Paciente, Doctor, HoraMedica
│   ├── views.py                 # Lógica de negocio (CRUD)
│   ├── forms.py                 # Formularios Django
│   ├── urls.py                  # Rutas de la app
│   └── admin.py                 # Registro en Django Admin
├── vitalcare/                   # Configuración del proyecto
│   ├── settings.py              # Configuración (lee desde .env)
│   └── urls.py                  # Rutas globales
├── .env                         # Variables de entorno (no en git)
├── .env.example                 # Plantilla de configuración
├── .gitignore
├── requirements.txt
└── manage.py
```

---

## 👥 Autores

- **Gabriela Alvarado Rosales**
- **Felipe Droguett Ortiz**
- **Rodrigo Villaroel Ugalde**

*Desarrolladores Fullstack en formación*

---

> Curso Full Stack Python · Kibernum IT Academy · 2026
