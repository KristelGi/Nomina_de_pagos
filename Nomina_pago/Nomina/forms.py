from django import forms
from .models import Empleado, Rol, Cargo,  Departamento, TipoContrato
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select, Textarea

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del empleado'}),
            'cedula': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12.345.678'}),
            'sexo': Select(attrs={'class': 'form-select'}, choices=[('', 'Seleccione género'), ('M', 'Masculino'), ('F', 'Femenino')]),
            'direccion': Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Dirección completa del empleado'}),
            'sueldo': NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'placeholder': '0.00'}),
            'cargo': Select(attrs={'class': 'form-select'}),
            'departamento': Select(attrs={'class': 'form-select'}),
            'tipo_contrato': Select(attrs={'class': 'form-select'})
        }
        



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
