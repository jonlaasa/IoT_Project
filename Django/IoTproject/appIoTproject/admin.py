from django.contrib import admin
from .models import Paciente, Familiar, PacienteFamiliarUnion
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(PacienteFamiliarUnion)