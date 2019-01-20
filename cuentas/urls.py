from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from cuentas.views import AddPersonView, AddCuentaView, ListCuentasView

urlpatterns = {
    url(r'^add_person/$', AddPersonView.as_view(), name="add_person"),
    url(r'^add_cuenta/$', AddCuentaView.as_view(), name="add_cuenta"),
    url(r'^get_cuentas/$', ListCuentasView.as_view(), name="get_cuentas")
    }

urlpatterns = format_suffix_patterns(urlpatterns)
