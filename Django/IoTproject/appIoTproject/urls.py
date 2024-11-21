from django.urls import path
from . import views  # Importa las vistas de la aplicación appIoTproject

urlpatterns = [
    path('', views.login_view, name='login'),  # Página principal para login
    path('pacientes/<str:id_familiar>/', views.pacientes_del_familiar, name='pacientes_del_familiar'),  # Muestra los pacientes asociados a un familiar
    path('escoger_paciente/', views.escoger_paciente, name='escoger_paciente'),  # Selección de un paciente específico
    path('paciente_info/<str:paciente_id>/', views.paciente_info, name='paciente_info'),  # Información detallada de un paciente
]
