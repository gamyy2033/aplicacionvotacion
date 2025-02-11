from django.shortcuts import render, get_object_or_404, redirect
from .models import PartidoPolitico, Cargo, Ubicacion, Recinto, Junta, Candidato, Votante
from .forms import PartidoForm, CargoForm, UbicacionForm, RecintoForm, JuntaForm, CandidatoForm, VotanteForm

# ==== PARTIDO POLÍTICO ====

def index(request):
    return render(request, 'base.html')
    
def listar_partidos(request):
    partidos = PartidoPolitico.objects.all()
    return render(request, 'listar_partidos.html', {'partidos': partidos})

def crear_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_partidos')
    else:
        form = PartidoForm()
    return render(request, 'crear_partido.html', {'form': form})

def editar_partido(request, pk):
    partido = get_object_or_404(PartidoPolitico, pk=pk)
    if request.method == 'POST':
        form = PartidoForm(request.POST, request.FILES, instance=partido)
        if form.is_valid():
            form.save()
            return redirect('listar_partidos')
    else:
        form = PartidoForm(instance=partido)
    return render(request, 'editar_partido.html', {'form': form})

def eliminar_partido(request, pk):
    partido = get_object_or_404(PartidoPolitico, pk=pk)
    partido.delete()
    return redirect('listar_partidos')

# ==== CARGO ====

def listar_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'listar_cargos.html', {'cargos': cargos})

def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
    else:
        form = CargoForm()
    return render(request, 'crear_cargo.html', {'form': form})

def editar_cargo(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'editar_cargo.html', {'form': form})

def eliminar_cargo(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    cargo.delete()
    return redirect('listar_cargos')

# ==== UBICACION ====

def listar_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'listar_ubicaciones.html', {'ubicaciones': ubicaciones})

def crear_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ubicaciones')
    else:
        form = UbicacionForm()
    return render(request, 'crear_ubicacion.html', {'form': form})

def editar_ubicacion(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return redirect('listar_ubicaciones')
    else:
        form = UbicacionForm(instance=ubicacion)
    return render(request, 'editar_ubicacion.html', {'form': form})

def eliminar_ubicacion(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    ubicacion.delete()
    return redirect('listar_ubicaciones')

# ==== RECINTO ====

def listar_recintos(request):
    recintos = Recinto.objects.all()
    return render(request, 'listar_recintos.html', {'recintos': recintos})

def crear_recinto(request):
    if request.method == 'POST':
        form = RecintoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_recintos')
    else:
        form = RecintoForm()
    return render(request, 'crear_recinto.html', {'form': form})

def editar_recinto(request, pk):
    recinto = get_object_or_404(Recinto, pk=pk)
    if request.method == 'POST':
        form = RecintoForm(request.POST, instance=recinto)
        if form.is_valid():
            form.save()
            return redirect('listar_recintos')
    else:
        form = RecintoForm(instance=recinto)
    return render(request, 'editar_recinto.html', {'form': form})

def eliminar_recinto(request, pk):
    recinto = get_object_or_404(Recinto, pk=pk)
    recinto.delete()
    return redirect('listar_recintos')

# ==== JUNTA ====

def listar_juntas(request):
    juntas = Junta.objects.all()
    return render(request, 'listar_juntas.html', {'juntas': juntas})

def crear_junta(request):
    if request.method == 'POST':
        form = JuntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_juntas')
    else:
        form = JuntaForm()
    return render(request, 'crear_junta.html', {'form': form})

def editar_junta(request, pk):
    junta = get_object_or_404(Junta, pk=pk)
    if request.method == 'POST':
        form = JuntaForm(request.POST, instance=junta)
        if form.is_valid():
            form.save()
            return redirect('listar_juntas')
    else:
        form = JuntaForm(instance=junta)
    return render(request, 'editar_junta.html', {'form': form})

def eliminar_junta(request, pk):
    junta = get_object_or_404(Junta, pk=pk)
    junta.delete()
    return redirect('listar_juntas')

# ==== CANDIDATO ====

def listar_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'listar_candidatos.html', {'candidatos': candidatos})

def crear_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_candidatos')
    else:
        form = CandidatoForm()
    return render(request, 'crear_candidato.html', {'form': form})

def editar_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('listar_candidatos')
    else:
        form = CandidatoForm(instance=candidato)
    return render(request, 'editar_candidato.html', {'form': form})

def eliminar_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    candidato.delete()
    return redirect('listar_candidatos')

# ==== VOTANTE ====

def listar_votantes(request):
    votantes = Votante.objects.all()
    return render(request, 'listar_votantes.html', {'votantes': votantes})

def crear_votante(request):
    if request.method == 'POST':
        form = VotanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_votantes')
    else:
        form = VotanteForm()
    return render(request, 'crear_votante.html', {'form': form})

def editar_votante(request, pk):
    votante = get_object_or_404(Votante, pk=pk)
    if request.method == 'POST':
        form = VotanteForm(request.POST, instance=votante)
        if form.is_valid():
            form.save()
            return redirect('listar_votantes')
    else:
        form = VotanteForm(instance=votante)
    return render(request, 'editar_votante.html', {'form': form})

def eliminar_votante(request, pk):
    votante = get_object_or_404(Votante, pk=pk)
    votante.delete()
    return redirect('listar_votantes')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Junta, Cargo, PartidoPolitico, Ubicacion, Recinto, Candidato, Votante
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings
import os

def reporte_general(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_general.pdf"'

    # Crear documento PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Título del reporte
    elements.append(Paragraph("Reporte General", styles['Title']))

    # Función para crear una tabla
    def crear_tabla(encabezados, datos, col_widths=None):
        tabla = Table([encabezados] + datos, colWidths=col_widths)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]))
        return tabla

    # Datos de Juntas Electorales
    juntas = Junta.objects.all()
    if juntas.exists():
        encabezados = ["Número de Junta", "Recinto"]
        datos = [[junta.numero, junta.recinto.nombre] for junta in juntas]
        elements.append(Paragraph("Juntas Electorales", styles['Heading2']))
        elements.append(crear_tabla(encabezados, datos))

    # Datos de Cargos
    cargos = Cargo.objects.all()
    if cargos.exists():
        encabezados = ["Nombre del Cargo"]
        datos = [[cargo.nombre] for cargo in cargos]
        elements.append(Paragraph("Cargos", styles['Heading2']))
        elements.append(crear_tabla(encabezados, datos))

    # Datos de Partidos Políticos
    partidos = PartidoPolitico.objects.all()
    if partidos.exists():
        encabezados = ["Nombre", "Siglas"]
        datos = [[partido.nombre, partido.siglas] for partido in partidos]
        elements.append(Paragraph("Partidos Políticos", styles['Heading2']))
        elements.append(crear_tabla(encabezados, datos))

    # Datos de Ubicaciones
    ubicaciones = Ubicacion.objects.all()
    if ubicaciones.exists():
        encabezados = ["Nombre", "Tipo"]
        datos = [[ubicacion.nombre, ubicacion.tipo] for ubicacion in ubicaciones]
        elements.append(Paragraph("Ubicaciones", styles['Heading2']))
        elements.append(crear_tabla(encabezados, datos))

    # Datos de Recintos
    recintos = Recinto.objects.all()
    if recintos.exists():
        encabezados = ["Nombre", "Ubicación"]
        datos = [[recinto.nombre, recinto.ubicacion.nombre] for recinto in recintos]
        elements.append(Paragraph("Recintos", styles['Heading2']))
        elements.append(crear_tabla(encabezados, datos))

    # Datos de Candidatos con Fotos y Logos
    candidatos = Candidato.objects.all()
    if candidatos.exists():
        encabezados = ["Foto", "Nombre", "Apellido", "Partido", "Logo", "Cargo"]
        datos = []

        for candidato in candidatos:
            fila = []

            # Imagen del candidato
            if candidato.foto:
                ruta_foto = os.path.join(settings.MEDIA_ROOT, str(candidato.foto))
                if os.path.exists(ruta_foto):
                    imagen_candidato = Image(ruta_foto, width=40, height=40)
                    fila.append(imagen_candidato)
                else:
                    fila.append("Sin foto")
            else:
                fila.append("Sin foto")

            fila.append(candidato.nombre)
            fila.append(candidato.apellido)
            fila.append(candidato.partido.nombre)

            # Logo del partido
            if candidato.partido.logo:
                ruta_logo = os.path.join(settings.MEDIA_ROOT, str(candidato.partido.logo))
                if os.path.exists(ruta_logo):
                    imagen_logo = Image(ruta_logo, width=40, height=40)
                    fila.append(imagen_logo)
                else:
                    fila.append("Sin logo")
            else:
                fila.append("Sin logo")

            fila.append(candidato.cargo.nombre)
            datos.append(fila)

        elements.append(Paragraph("Candidatos", styles['Heading2']))
        elements.append(crear_tabla(encabezados, datos, col_widths=[50, 100, 100, 100, 50, 100]))

    # Datos de Votantes
    votantes = Votante.objects.all()
    if votantes.exists():
        encabezados = ["Cédula", "Nombre", "Apellido", "Junta"]
        datos = [[votante.cedula, votante.nombre, votante.apellido, votante.junta.numero] for votante in votantes]
        elements.append(Paragraph("Votantes", styles['Heading2']))
        elements.append(crear_tabla(encabezados, datos))

    # Construcción del PDF
    doc.build(elements)
    return response
