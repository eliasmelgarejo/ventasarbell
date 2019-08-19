from django.contrib import admin

from django.contrib.admin.decorators import register

# Register your models here.
from stock.form import LineaForm
from stock.models import Linea, Producto, Deposito, ProductoDeposito


@register(Linea)
class LineaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    list_filter = ('codigo', 'nombre',)
    search_fields = ['codigo', 'nombre']


@register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    form = LineaForm
    list_display = ('codigo', 'nombre', 'linea', 'activo',)
    list_filter = ('codigo', 'nombre',)
    search_fields = ['codigo', 'nombre']


@register(Deposito)
class DepositoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    list_filter = ('codigo', 'nombre',)
    search_fields = ['codigo', 'nombre']


@register(ProductoDeposito)
class ProductoDepositoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'deposito', 'stock',)
    list_filter = ('producto', 'deposito', 'stock',)
    search_fields = ('producto', 'deposito',)
