class EstadoSolicitud:
    ABIERTO = 'ABIERTO'
    CERRADO = 'CERRADO'
    CANCELADO = 'CANCELADO'

    LISTA_ESTADOS_PEDIDOS = (
        (ABIERTO, 'Abierto'),
        (CERRADO, 'Cerrado'),
        (CANCELADO, 'Cancelado'),
    )


class EstadoSolicitudDetalle:
    EN_ESPERA = 'EN_ESPERA'
    RECIBIDO = 'RECIBIDO'
    ENTREGADO = 'ENTREGADO'
    COBRADO = 'COBRADO'
    CANCELADO = 'CANCELADO'
    DEVUELTO = 'DEVUELTO'

    LISTA_ESTADOS_PEDIDOS_DETALLE = (
        (EN_ESPERA, 'EnEspera'),
        (RECIBIDO, 'Recibido'),
        (ENTREGADO, 'Entregado'),
        (COBRADO, 'Cobrado'),
        (CANCELADO, 'Cancelado'),
        (DEVUELTO, 'Devuelto'),
    )