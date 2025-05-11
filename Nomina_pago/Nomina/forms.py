from django import forms
from .models import Empleado, Rol, Cargo,  Departamento, TipoContrato


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        
class TipoContratoForm(forms.ModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'
        


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        exclude = ['sueldo', 'iess', 'tot_ing', 'tot_des', 'neto']
        widgets = {
            'aniomes': forms.DateInput(attrs={'type': 'date'})
        }
