from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Nomina.models import Empleado, Rol, Cargo, Departamento, TipoContrato

admin.site.site_header = "App Nómina"
admin.site.site_title = "App Nómina Admin"

admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(TipoContrato)
