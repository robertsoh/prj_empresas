from django.contrib import admin

from apps.empresa.models import Empresa, TipoContribuyente


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'nombre', 'tipo_contribuyente', 'estado', 'condicion')
    search_fields = ('ruc', 'nombre')


@admin.register(TipoContribuyente)
class TipoContribuyenteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
