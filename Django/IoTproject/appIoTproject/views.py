from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import Paciente, Familiar, PacienteFamiliarUnion

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')

        print(f"Datos recibidos: Usuario: '{usuario}', Contraseña: '{contraseña}'")

        if not usuario or not contraseña:
            return render(request, 'index.html', {'error': 'Por favor, ingrese usuario y contraseña'})

        try:
            familiar = Familiar.objects.get(usuario=usuario)
        except Familiar.DoesNotExist:
            return render(request, 'index.html', {'error': 'Usuario o contraseña incorrectos'})

        # Comparar la contraseña como texto plano
        if familiar.contraseña == contraseña:  # Aquí comparamos las contraseñas directamente
            # Si las contraseñas coinciden, obtienes los pacientes
            pacientes_union = PacienteFamiliarUnion.objects.select_related('paciente').filter(familiar=familiar)
            pacientes = [union.paciente for union in pacientes_union]
            return render(request, 'escoger_paciente.html', {'pacientes': pacientes})

        # Si la contraseña no coincide
        return render(request, 'index.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'index.html')




def pacientes_del_familiar(request, id_familiar):
    familiar = get_object_or_404(Familiar, id=id_familiar)
    
    # Optimización con select_related
    pacientes_union = PacienteFamiliarUnion.objects.select_related('paciente').filter(familiar=familiar)
    pacientes_data = [
        {
            "id": union.paciente.id,
            "nombre": union.paciente.nombre,
            "apellido": union.paciente.apellido,
            "hear_rate": union.paciente.hear_rate,
            "o2_sangre": union.paciente.o2_sangre,
            "temperatura_corporal": union.paciente.temperatura_corporal,
            "tiempo_tomado": union.paciente.tiempo_tomado,
            "direccion": union.paciente.direccion,
        }
        for union in pacientes_union
    ]
    return JsonResponse({"pacientes": pacientes_data})

def escoger_paciente(request):
    # Aquí puedes incluir la lógica para seleccionar el paciente
    return render(request, 'escoger_paciente.html')

def paciente_info(request, paciente_id):
    # Intentamos obtener el paciente con el ID proporcionado
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'paciente_info.html', {'paciente': paciente})


def paciente_panel_hr(request, paciente_id):
    # Intentamos obtener el paciente con el ID proporcionado
    paciente = get_object_or_404(Paciente, id=paciente_id)
    # Renderizamos el template con el iframe, pasando el ID del paciente como contexto
    return render(request, 'paciente_panel_hr.html', {'paciente_id': paciente.id})

def paciente_panel_o2(request, paciente_id):
    # Intentamos obtener el paciente con el ID proporcionado
    paciente = get_object_or_404(Paciente, id=paciente_id)
    # Renderizamos el template específico para el panel de O2
    return render(request, 'paciente_panel_o2.html', {'paciente_id': paciente.id})

def paciente_panel_temp(request, paciente_id):
    # Intentamos obtener el paciente con el ID proporcionado
    paciente = get_object_or_404(Paciente, id=paciente_id)
    # Renderizamos el template específico para el panel de O2
    return render(request, 'paciente_panel_temp.html', {'paciente_id': paciente.id})

