
from django.shortcuts import get_object_or_404, render, redirect
from .models import Empleado, Rol, Departamento, Cargo, TipoContrato
from .forms import EmpleadoForm, RolForm, CargoForm, DepartamentoForm, TipoContratoForm
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return HttpResponse("Bienvenido al Home")

def crear_empleado(request):
    contexto= {"tittle": "Ingrese un Empleado"}
    print("metodo: ", request.method)
    if request.method == "GET":
        print("entro por get")
        form = EmpleadoForm()
        contexto['form'] = form
        return render(request, 'empleado/create.html', contexto)
    else:
       print("entro por post")
       form = EmpleadoForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('Nomina:listar_empleados')
       else:
           contexto['form'] = form
           return render(request, 'empleado/create.html',contexto) 

    
def listar_empleados(request):
    query = request.GET.get('q', '')
    depto_id = request.GET.get('departamento', '')
    cargo_id = request.GET.get('cargo', '')
    contrato_id = request.GET.get('contrato', '')



    empleados = Empleado.objects.all()

    if query:
        empleados = empleados.filter(nombre__icontains=query)

    if depto_id:
        empleados = empleados.filter(departamento_id=depto_id)
    
    if cargo_id:
        empleados = empleados.filter(cargo_id=cargo_id)
    
    if contrato_id:
        empleados = empleados.filter(tipo_contrato_id=contrato_id)
        
    

    departamentos = Departamento.objects.all()
    cargos = Cargo.objects.all()
    tipos_contrato = TipoContrato.objects.all()
    
    contexto = {
        'empleados': empleados,
        'departamentos': departamentos,
        'cargos': cargos,
        'q': query,
        'departamento_seleccionado': depto_id,
        'cargo_seleccionado': cargo_id,
        'tipos_contrato': tipos_contrato,
        'contrato_seleccionado': contrato_id,
        'title': 'Listado de empleados'
    }

    return render(request, 'empleado/list.html', contexto)

    


def actualizar_empleado(request, id):
    contexto = {'title': "Actualizar Empleado"}
    empleado = get_object_or_404(Empleado, pk=id)

    if request.method == "GET":
        form = EmpleadoForm(instance=empleado)
        contexto['form'] = form
        return render(request, 'empleado/update.html', contexto)

    else:
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_empleados') 
        else:
            contexto['form'] = form
            return render(request, 'empleado/update.html', contexto)




def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)

    if request.method == "GET":
        contexto = {
            'title': 'Empleado a Eliminar',
            'empleado': empleado,
            'error': ''
        }
        return render(request, 'empleado/delete.html', contexto)

    else:  
        empleado.delete()
        # messages.success(request, 'Empleado eliminado correctamente.')
        return redirect('Nomina:listar_empleados')
    
########################### Cargos ##################################

def crear_cargo(request):
    contexto = {'title': 'Crear Cargo'}
    if request.method == 'GET':
        form= CargoForm()
        contexto['form'] = form
        return render(request, 'cargo/create.html', contexto)
    else:
        form= CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_cargos')
        else:
            contexto['form'] = form
            return render(request, 'cargo/create.html', contexto)

def listar_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'cargo/list.html', {'cargos': cargos, 'title': 'Listado de Cargos'})

def actualizar_cargo(request, id):
    cargo = get_object_or_404(Cargo, pk=id)
    contexto = {'title': 'Actualizar Cargo'}
    if request.method == 'GET':
        form = CargoForm(instance=cargo)
        contexto['form'] = form
        return render(request, 'cargo/update.html', contexto)
    else:
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_cargos')
        else:
            contexto['form'] = form
            return render(request, 'cargo/update.html', contexto)

def eliminar_cargo(request, id):
    cargo = get_object_or_404(Cargo, pk=id)
    if request.method == 'POST':
        cargo.delete()
        return redirect('Nomina:listar_cargos')
    return render(request, 'cargo/delete.html', {'cargo': cargo, 'title': 'Eliminar Cargo'})

############################## Departamentos ###########################

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamento/list.html', {
        'departamentos': departamentos,
        'title': 'Listado de Departamentos'
    })

def crear_departamento(request):
    contexto = {'title': 'Crear Departamento'}
    if request.method == 'GET':
        form = DepartamentoForm()
        contexto['form'] = form
        return render(request, 'departamento/create.html', contexto)
    else:
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_departamentos')
        else:
            contexto['form'] = form
            return render(request, 'departamento/create.html', contexto)

def actualizar_departamento(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    contexto = {'title': 'Actualizar Departamento'}
    if request.method == 'GET':
        form = DepartamentoForm(instance=departamento)
        contexto['form'] = form
        return render(request, 'departamento/update.html', contexto)
    else:
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_departamentos')
        else:
            contexto['form'] = form
            return render(request, 'departamento/update.html', contexto)

def eliminar_departamento(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('Nomina:listar_departamentos')
    return render(request, 'departamento/delete.html', {
        'departamento': departamento,
        'title': 'Eliminar Departamento'
    })

###############################Tipo de Contrato############################

def listar_tipos_contrato(request):
    contratos = TipoContrato.objects.all()
    return render(request, 'contrato/list.html', {
        'contratos': contratos,
        'title': 'Listado de Tipos de Contrato'
    })

def crear_tipo_contrato(request):
    contexto = {'title': 'Crear Tipo de Contrato'}
    if request.method == 'GET':
        form = TipoContratoForm()
        contexto['form'] = form
        return render(request, 'contrato/create.html', contexto)
    else:
        form = TipoContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_tipos_contrato')
        else:
            contexto['form'] = form
            return render(request, 'contrato/create.html', contexto)

def actualizar_tipo_contrato(request, id):
    contrato = get_object_or_404(TipoContrato, pk=id)
    contexto = {'title': 'Actualizar Tipo de Contrato'}
    if request.method == 'GET':
        form = TipoContratoForm(instance=contrato)
        contexto['form'] = form
        return render(request, 'contrato/update.html', contexto)
    else:
        form = TipoContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_tipos_contrato')
        else:
            contexto['form'] = form
            return render(request, 'contrato/update.html', contexto)

def eliminar_tipo_contrato(request, id):
    contrato = get_object_or_404(TipoContrato, pk=id)
    if request.method == 'POST':
        contrato.delete()
        return redirect('Nomina:listar_tipos_contrato')
    return render(request, 'contrato/delete.html', {
        'contrato': contrato,
        'title': 'Eliminar Tipo de Contrato'
    })


############################# Rol #######################################

def listar_roles(request):
    query = request.GET.get('q', '')
    mes = request.GET.get('mes', '')
    sueldo_min = request.GET.get('sueldo_min', '')

    roles = Rol.objects.select_related('empleado').all()

    if query:
        roles = roles.filter(empleado__nombre__icontains=query)

    if mes:
        try:
            mes_int = int(mes)
            roles = roles.filter(aniomes__month=mes_int)
        except ValueError:
            print("⚠️ Mes inválido: no se aplicó filtro por mes")

    if sueldo_min:
        try:
            sueldo_val = float(sueldo_min)
            roles = roles.filter(sueldo__gte=sueldo_val)
        except ValueError:
            print("Sueldo mínimo inválido: no se aplicó filtro")

    contexto = {
        'roles': roles,
        'title': 'Listado de Roles',
        'q': query,
        'mes': mes,
        'sueldo_min': sueldo_min,
    }

    return render(request, 'rol/list.html', contexto)


def crear_rol(request):
    contexto = {'title': 'Crear Rol'}
    if request.method == 'GET':
        form = RolForm()
        contexto['form'] = form
        return render(request, 'rol/create.html', contexto)
    else:
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_roles')
        else:
            contexto['form'] = form
            return render(request, 'rol/create.html', contexto)

def actualizar_rol(request, id):
    rol = get_object_or_404(Rol, pk=id)
    contexto = {'title': 'Actualizar Rol'}
    if request.method == 'GET':
        form = RolForm(instance=rol)
        contexto['form'] = form
        return render(request, 'rol/update.html', contexto)
    else:
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('Nomina:listar_roles')
        else:
            contexto['form'] = form
            return render(request, 'rol/update.html', contexto)

def eliminar_rol(request, id):
    rol = get_object_or_404(Rol, pk=id)
    if request.method == 'POST':
        rol.delete()
        return redirect('Nomina:listar_roles')
    return render(request, 'rol/delete.html', {'rol': rol, 'title': 'Eliminar Rol'})
