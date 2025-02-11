from django import forms
from .models import PartidoPolitico, Candidato, Ubicacion, Recinto, Junta, Cargo, Votante

class PartidoForm(forms.ModelForm):
    class Meta:
        model = PartidoPolitico
        fields = ['nombre', 'siglas', 'logo']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre']

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nombre', 'apellido', 'partido', 'cargo', 'foto']

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'tipo']

class RecintoForm(forms.ModelForm):
    class Meta:
        model = Recinto
        fields = ['nombre', 'ubicacion']

class JuntaForm(forms.ModelForm):
    class Meta:
        model = Junta
        fields = ['numero', 'recinto']

class VotanteForm(forms.ModelForm):
    class Meta:
        model = Votante
        fields = ['cedula', 'nombre', 'apellido', 'junta']


class ReporteForm(forms.Form):
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    categoria = forms.ChoiceField(choices=[('', 'Todos'), ('presidente', 'Presidente'), ('vicepresidente', 'Vicepresidente')], required=False)