"""ventasarbell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from stock.autocomplete import LineaAutocomplete

urlpatterns = [
    url(
        r'^admin/', include(admin.site.urls)),

    url(
        r'^', include(admin.site.urls)),

    url(
        r'^linea-autocomplete/$',
        LineaAutocomplete.as_view(),
        name='linea-autocomplete',
    ),
]


admin.site.site_header = "Ventas ARBELL"
admin.site.site_title = "Gestión de Pedidos, Cobros, Entregas"
admin.site.site_name = "ARBELLAPP"