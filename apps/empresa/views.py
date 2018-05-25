from django.contrib import messages
from django.views.generic import ListView

from apps.common import sunat
from apps.empresa.models import Empresa


class EmpresaListView(ListView):
    template_name = 'empresa/list.html'
    model = Empresa
    context_object_name = 'empresas'

    def get_queryset(self):
        q = self.request.GET.get('q')
        data = sunat.buscar_ruc(q)
        if not q:
            messages.warning(self.request, 'Ingrese el ruc a buscar')
            return Empresa.objects.none()
        qs = Empresa.objects.filter(ruc=q)
        if not qs:
            data = sunat.buscar_ruc(q)
            if data:
                try:
                    empresa = Empresa.objects.create(**data)
                    return Empresa.objects.filter(id=empresa.id)
                except Exception:
                    messages.warning(self.request, 'Error al crear la empresa')
            else:
                messages.warning(self.request, 'No se encontraron coincidencias')
        return qs
