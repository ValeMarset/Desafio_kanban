from app import models, columns


class DetalleRecibos(models.Model):
	_table = 'detalle_recibos'  # nombre de la tabla en base de datos
	_description = 'Detalle de Recibos'  # nombre del modelo en lenguaje humano

	# columnas de la tabla (la columna ID es implícita)
	_columns = {
		'tipoConcepto': columns.VarChar('Tipo Concepto'),
		'cantidad': columns.Integer('Cantidad'),
		'monto': columns.Decimal('Monto')
	}
