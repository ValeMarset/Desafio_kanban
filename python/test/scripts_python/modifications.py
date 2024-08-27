import app
from app.models.funcionarios import Funcionario
from app.models.recibos_sueldo import RecibosSueldo
from app.models.detalle_recibos import DetalleRecibos

def eliminar_recibos_por_cedula(cedula):
    recibos = models.RecibosSueldo.records()
    for recibo in recibos:
        if recibo.cedulaFuncionario == cedula:
            recibo.delete()

def modificar_funcionario(cedula, nuevo_nombre, nuevo_cargo):
    funcionarios = models.Funcionario.records()
    for funcionario in funcionarios:
        if funcionario.cedula == cedula:
            funcionario.update({
                'nombre': nuevo_nombre,
                'cargo': nuevo_cargo
            })
