import app
from app import models, columns
from models.funcionarios import Funcionario
from models.detalleRecibos import DetalleRecibos


class RecibosSueldo(models.Model):
	_table = 'recibos_sueldo'  # Nombre de la tabla en base de datos
	_description = 'Recibos de Sueldo'  # Nombre del modelo en lenguaje humano

	# El código a continuación representa un intento inicial para definir las relaciones entre
	# el modelo 'RecibosSueldo' y los modelos relacionados 'Funcionario' y 'DetalleRecibos'.
	# Sin embargo, este enfoque resultó en un error que no se pudo resolver en el momento.
	# Las relaciones intentadas eran:
	# - Asociar cada recibo de sueldo con un funcionario a través del campo 'cedulaFuncionario'.
	# - Asociar cada recibo de sueldo con los detalles del recibo a través del campo 'detalleReciboId'.
	#
	# Las relaciones se definieron como sigue:
	# - 'detalleReciboId': relación con el modelo 'DetalleRecibos'.
	# - 'cedulaFuncionario': relación con el modelo 'Funcionario'.

	_columns = {
	    'anioMes': columns.VarChar('Año/Mes'),
	    'tipoRecibo': columns.VarChar('Tipo Recibo'),
	    'cedulaFuncionario': columns.Integer('Cédula Funcionario'),
	    'nombreEmpleador': columns.VarChar('Nombre Empleador'),
	    'detalleReciboId': columns.Integer('ID Detalle Recibo')
	}

	# _columns = {
	# 	'anioMes': columns.VarChar('Año / Mes'),
	# 	'tipoRecibo': columns.VarChar('Tipo Recibo'),
	# 	'cedulaFuncionario': columns.Relation('Cedula', [Funcionario]),
	# 	'nombreEmpleador': columns.VarChar('Nombre Empleador'),
	# 	'detalleReciboId': columns.Relation('Detalle Recibos', [DetalleRecibos])
	# }
