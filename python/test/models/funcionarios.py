import app
from app import models, columns


class Funcionario(models.Model):
	_table = 'funcionarios'  # nombre de la tabla en base de datos
	_description = 'Funcionario'  # nombre del modelo en lenguaje humano

	# columnas de la tabla (la columna ID es implícita)
	_columns = {
		'cedula': columns.VarChar('Cedula'),
		'nombre': columns.VarChar('Nombre'),
		'cargo': columns.VarChar('Cargo'),
		'sueldo': columns.Decimal('Sueldo'),
		'fechaIngreso': columns.VarChar('Fecha Ingreso')
	}
