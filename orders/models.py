from django.db import models

# Create your models here.
from orders.constants import EstadoSolicitud, EstadoSolicitudDetalle
from stock.models import Producto


class Pedido(models.Model):
    fechaPedido = models.DateField(verbose_name="Fecha")
    fechaCierre = models.DateField(verbose_name="Cierre")
    totalCosto = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                     verbose_name="Costo")
    totalVenta = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                     verbose_name="Venta")
    totalGanancia = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                        verbose_name="Ganancia")
    totalPagado = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                      verbose_name="Pagado")
    totalCobrado = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                       verbose_name="Cobrado")
    totalSaldo = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                     verbose_name="Saldo")
    estado = models.CharField(max_length=255, choices=EstadoSolicitud.LISTA_ESTADOS_PEDIDOS,
                              default=EstadoSolicitud.ABIERTO, verbose_name="Estado")

    class Meta:
        ordering = ["fechaPedido"]
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return str(self.fechaPedido)


class PedidoDetalle(models.Model):
    item = models.IntegerField(verbose_name="Item")
    cliente = models.CharField(verbose_name="Cliente")
    producto = models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                verbose_name="Costo")
    venta = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                verbose_name="Venta")
    ganancia = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                   verbose_name="Ganancia")
    cantidad = models.IntegerField(default=1, verbose_name="Cantidad")
    unitario = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                   verbose_name="P.Unitario")
    total = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                verbose_name="Total")
    neto = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                               verbose_name="Neto")
    descuento = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                    verbose_name="Descuento")
    pagado = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                 verbose_name="Pagado")
    cobrado = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                  verbose_name="Cobrado")
    saldo = models.DecimalField(max_digits=10, decimal_places=10, default=0.0, null=True, blank=True,
                                verbose_name="Saldo")
    rendido = models.BooleanField(default=False, verbose_name="Rendido")
    fechaSolicitado = models.DateField(verbose_name="F.Solicitado")
    fechaEntrega = models.DateField(verbose_name="F.Entrega")
    fechaCancelacion = models.DateField(verbose_name="F.Cancelación")
    fechaRendido = models.DateField(verbose_name="F.Rendido")
    estado = models.CharField(choices=EstadoSolicitudDetalle.LISTA_ESTADOS_PEDIDOS_DETALLE,
                              default=EstadoSolicitudDetalle.EN_ESPERA, verbose_name="Estado")

    class Meta:
        ordering = ["item"]
        verbose_name_plural = "Detalles"

    def __str__(self):
        return str(self.item) + "-" + str(self.producto)

