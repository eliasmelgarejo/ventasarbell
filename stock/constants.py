class TipoMovimiento:
    ALTA = 'ALTA'
    BAJA = 'BAJA'
    TRANSLADO = 'TRANSLADO'

    LISTA_TIPOS_MOVIMIENTOS = (
        (ALTA, 'Alta'),
        (BAJA, 'Baja'),
        (TRANSLADO, 'Translado'),
    )


class UnidadMedida:
    UNIDAD = 'UNIDAD'
    LITRO = 'LITRO'

    LISTA_UNIDADES_MEDIDAS = (
        (UNIDAD, 'Unidad'),
        (LITRO, 'Litro'),
    )

