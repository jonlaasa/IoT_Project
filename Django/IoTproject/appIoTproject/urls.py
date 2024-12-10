from django.urls import path
from . import views  # Importa las vistas de la aplicación appIoTproject

urlpatterns = [
    path('', views.login_view, name='login'),  # Página principal para login
    path('pacientes/<str:id_familiar>/', views.pacientes_del_familiar, name='pacientes_del_familiar'),  # Muestra los pacientes asociados a un familiar
    path('escoger_paciente/', views.escoger_paciente, name='escoger_paciente'),  # Selección de un paciente específico
    path('paciente_info/<str:paciente_id>/', views.paciente_info, name='paciente_info'),  # Información detallada de un paciente
    path('paciente/<int:paciente_id>/panelhr/', views.paciente_panel_hr, name='paciente_panel_hr'),
    path('paciente/<int:paciente_id>/panelo2/', views.paciente_panel_o2, name='paciente_panel_o2'),
    path('paciente/<int:paciente_id>/paneltemp/', views.paciente_panel_temp, name='paciente_panel_temp'),

]
