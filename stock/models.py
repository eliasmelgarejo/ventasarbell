from django.utils import timezone
from django.db import models

# Create your models here.
from stock.constants import TipoMovimiento, UnidadMedida


class Linea(models.Model):
    codigo = models.CharField(max_length=255, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=255, verbose_name="Nombre")

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Lineas"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo = models.CharField(max_length=255, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    linea = models.ForeignKey(Linea, verbose_name="Linea")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    imagen = models.ImageField(upload_to="imagen")

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.codigo + "-" + self.nombre


class Deposito(models.Model):
    codigo = models.CharField(max_length=255, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=255, verbose_name="Nombre")

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Depositos"

    def __str__(self):
        return self.nombre


class ProductoDeposito(models.Model):
    producto = models.ForeignKey(Producto, verbose_name="Producto")
    deposito = models.ForeignKey(Deposito, verbose_name="Depósito")
    stock = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, verbose_name="Stock", null=True,
                                blank=True)
    unidadmedida = models.CharField(choices=UnidadMedida.LISTA_UNIDADES_MEDIDAS, default=UnidadMedida.UNIDAD,
                                    verbose_name="Unidad Medida", max_length=30)

    class Meta:
        ordering = ["deposito"]
        verbose_name_plural = "Prod. x Depositos"

    def __str__(self):
        return self.producto + "-" + self.deposito


class MovimientoProducto(models.Model):
    producto = models.ForeignKey(Producto,  verbose_name="Producto")
    deposito = models.ForeignKey(Deposito, verbose_name="Depósito")
    tipomovimiento = models.CharField(choices=TipoMovimiento.LISTA_TIPOS_MOVIMIENTOS, verbose_name="Tipo Movimiento",
                                      max_length=20)
    cantidad = models.DecimalField(max_digits=2, decimal_places=0, default=0.0, verbose_name="Stock")
    fecha = models.DateField(default=timezone.now, verbose_name="Fecha")
    campaña = models.CharField(max_length=255, verbose_name="Campaña")

    class Meta:
        ordering = ["producto"]
        verbose_name_plural = "Movimiento Prod."

    def __str__(self):
        return self.tipomovimiento + "#" + self.producto + ": " + str(self.cantidad)
