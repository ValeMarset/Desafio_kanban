import csv
import app
from app.models.funcionarios import Funcionario
from app.models.recibosSueldo import RecibosSueldo
from app.models.detalleRecibos import DetalleRecibos

def cargar_funcionarios(filepath):
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)

            funcionarios_creados = []

            for row in reader:
                print(row)
                try:
                    Funcionario = app.env['funcionario_funcionario']
                    funcionario = Funcionario.create({
                        'cedula': row['cedula'],
                        'nombre': row['nombre'],
                        'cargo': row['cargo'],
                        'sueldo': row['sueldo'],
                        'fechaIngreso': row['fechaIngreso']
                    })
                    print(f"Funcionario {row['nombre']} cargado con éxito.")
                except Exception as e:
                    print(f"Error al cargar funcionario {row['nombre']}: {e}")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}")
    except Exception as e:
        print(f"Error al abrir el archivo {filepath}: {e}")

def cargar_recibos(filepath):
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    models.RecibosSueldo.create({
                        'anioMes': row['anioMes'],
                        'tipoRecibo': row['tipoRecibo'],
                        'cedulaFuncionario': row['cedulaFuncionario'],
                        'nombreEmpleador': row['nombreEmpleador'],
                        'detalleReciboId': row['detalleReciboId']
                    })
                    print(f"Recibo de sueldo para el funcionario {row['cedulaFuncionario']} cargado con éxito.")
                except Exception as e:
                    print(f"Error al cargar recibo de sueldo para el funcionario {row['cedulaFuncionario']}: {e}")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}")
    except Exception as e:
        print(f"Error al abrir el archivo {filepath}: {e}")

def cargar_detalle_recibos(filepath):
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    models.DetalleRecibos.create({
                        'tipoConcepto': row['tipoConcepto'],
                        'cantidad': row['cantidad'],
                        'monto': row['monto'],
                    })
                    print(f"Detalle del recibo de sueldo cargado con éxito.")
                except Exception as e:
                    print(f"Error al cargar detalle del recibo de sueldo: {e}")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}")
    except Exception as e:
        print(f"Error al abrir el archivo {filepath}: {e}")