from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # === PARTIDO POLÍTICO ===
    path('partidos/', views.listar_partidos, name='listar_partidos'),
    path('partidos/crear/', views.crear_partido, name='crear_partido'),
    path('partidos/editar/<int:pk>/', views.editar_partido, name='editar_partido'),
    path('partidos/eliminar/<int:pk>/', views.eliminar_partido, name='eliminar_partido'),

    # === CARGO ===
    path('cargos/', views.listar_cargos, name='listar_cargos'),
    path('cargos/crear/', views.crear_cargo, name='crear_cargo'),
    path('cargos/editar/<int:pk>/', views.editar_cargo, name='editar_cargo'),
    path('cargos/eliminar/<int:pk>/', views.eliminar_cargo, name='eliminar_cargo'),

    # === UBICACION ===
    path('ubicaciones/', views.listar_ubicaciones, name='listar_ubicaciones'),
    path('ubicaciones/crear/', views.crear_ubicacion, name='crear_ubicacion'),
    path('ubicaciones/editar/<int:pk>/', views.editar_ubicacion, name='editar_ubicacion'),
    path('ubicaciones/eliminar/<int:pk>/', views.eliminar_ubicacion, name='eliminar_ubicacion'),

    # === RECINTO ===
    path('recintos/', views.listar_recintos, name='listar_recintos'),
    path('recintos/crear/', views.crear_recinto, name='crear_recinto'),
    path('recintos/editar/<int:pk>/', views.editar_recinto, name='editar_recinto'),
    path('recintos/eliminar/<int:pk>/', views.eliminar_recinto, name='eliminar_recinto'),

    # === JUNTA ===
    path('juntas/', views.listar_juntas, name='listar_juntas'),
    path('juntas/crear/', views.crear_junta, name='crear_junta'),
    path('juntas/editar/<int:pk>/', views.editar_junta, name='editar_junta'),
    path('juntas/eliminar/<int:pk>/', views.eliminar_junta, name='eliminar_junta'),

    # === CANDIDATO ===
    path('candidatos/', views.listar_candidatos, name='listar_candidatos'),
    path('candidatos/crear/', views.crear_candidato, name='crear_candidato'),
    path('candidatos/editar/<int:pk>/', views.editar_candidato, name='editar_candidato'),
    path('candidatos/eliminar/<int:pk>/', views.eliminar_candidato, name='eliminar_candidato'),

    # === VOTANTE ===
    path('votantes/', views.listar_votantes, name='listar_votantes'),
    path('votantes/crear/', views.crear_votante, name='crear_votante'),
    path('votantes/editar/<int:pk>/', views.editar_votante, name='editar_votante'),
    path('votantes/eliminar/<int:pk>/', views.eliminar_votante, name='eliminar_votante'),
     
    path('reporte_general/', views.reporte_general, name='reporte_general'),
]


