from django.conf.urls import url

from apps.empresa.views import EmpresaListView

urlpatterns = [
    url(r'^buscar/$', EmpresaListView.as_view(), name='list'),
]
