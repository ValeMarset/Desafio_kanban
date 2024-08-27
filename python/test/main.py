import app
import csv
# from scripts.ingest_datos import cargar_funcionarios, cargar_recibos, cargar_detalle_recibos
# from scripts.modifications import eliminar_recibos_por_cedula, modificar_funcionario

print('\napp.env almacena el entorno de la aplicacion, desde donde se puede acceder a la definición de los modelos de la siguiente forma:')
Car = app.env['car_car']
print(Car)

print('\nEl método create recibe un diccionario de valores y retorna una instancia del modelo para el registro que acaba de crear:')
car = Car.create({'color': 'Rojo', 'brand': 'Hyundai'})
print(car)
print(car.seats_count)

seats = []
print(seats)
for i in range(1, 5):
  seats.append(app.env['car_seat'].create({'car_id': car.id}))
  print(seats)

print('\nSe puede acceder a las columnas de un modelo como atributos e incluso actualizarlas:')
car.seats_count = len(seats)
print(car.seats_count)

print('\nEl método records retorna todos los registros existentes para el modelo indicado como una lista de instancias:')
all_seats = app.env['car_seat'].records()
print(all_seats)

print('\nEl método read retorna los valores de todas las columnas de un registro como un diccionario:')
for seat in all_seats:
  print(seat.read())

print('\nEl método browse retorna el regsitro del modelo según el ID recibido - también puede recibir lista de IDs, en cuyo caso retorna una lista de registros:')
car_again = Car.browse(all_seats[0].car_id.id)
print(car_again)
print(car.read() == car_again.read())
del car_again

print('\nEl método update recibe un diccionario de valores y actualiza las columnas del registro con los nuevos valores:')
print(car.read())
car.update({'color': 'Azul', 'open_ceiling': True})
print(car.read())

print('\nEl método delete elimina el registro en base de datos:')
for seat in all_seats:
  seat.delete()
car.delete()
print(Car.records())
print(app.env['car_seat'].records())


def cargar_funcionarios(filepath):
  try:
    with open(filepath, mode='r') as file:
      reader = csv.DictReader(file)
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
        print(row)
        try:
          RecibosSueldo = app.env['recibos_sueldo']
          recibos = RecibosSueldo.create({
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
        print(row)
        try:
          DetalleRecibos = app.env['detalle_recibos']
          detalle = DetalleRecibos.create({
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

## Modificaciones:
  def eliminar_recibos_por_cedula(cedula):
    recibos = RecibosSueldo.records()
    for recibo in recibos:
      if recibo.cedulaFuncionario == cedula:
        recibo.delete()
    print(recibo)

def modificar_funcionario(cedula, nuevo_nombre, nuevo_cargo):
  funcionarios = app.env['nuevo_funcionario'].records()
  for funcionario in funcionarios:
    if funcionario.cedula == cedula:
      funcionario.update({
        'nombre': nuevo_nombre,
        'cargo': nuevo_cargo
      })
  print(funcionarios)


def main():
  # Cargar datos desde los archivos CSV
  print("\nCargando datos iniciales desde archivos CSV...")
  cargar_funcionarios('data/funcionarios.csv')
  cargar_recibos('data/recibos_sueldo.csv')
  cargar_detalle_recibos('data/detalle_recibos.csv')

  # Modificación de ejemplo
  print("\nModificando datos de un funcionario...")
  modificar_funcionario('12345678', 'Juan Jose Perez', 'Analista de Datos')
  print("Funcionario modificado con éxito.")

  # Eliminar recibos de un funcionario
  print("\nEliminando recibos de sueldo...")
  eliminar_recibos_por_cedula('12345678')
  print("Recibos de sueldo eliminados con éxito.")



if __name__ == '__main__':
  main()