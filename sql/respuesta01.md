### Analice la siguiente consulta SQL y explique lo que se obtiene con la misma:

   ~~~
    SELECT
    fecha_renta,
    titulo,
    genero,
    cantidad_pagada,
    RANK() OVER(PARTITION BY genero ORDER BY cantidad_pagada DESC)
    FROM pelicula
    JOIN alquiler
    ON alquiler.pelicula_id = pelicula.id;
   ~~~

- Lo que se obtendrá de la consulta son cinco columnas: 'fecha_renta', 'titulo', 'genero', 'cantidad_pagada', y una columna extra que muestra el rango de cada película dentro de su género según la cantidad_pagada. Cada género formará un grupo independiente, y dentro de cada grupo, las películas estarán clasificadas según el monto pagado, asignando un rango a cada una de ellas según si el monto es mayor o menor. Si el monto pagado es mayor, la película recibirá un rango más alto (número más bajo). Si hubiera varios montos iguales, se les asignaría el mismo rango a las películas que los compartan.

#### Hecho lo anterior, diseñe tabla de Clientes con al menos 3 campos y arme una nueva consulta que incorpore datos de estos, ordenados por nombre de película y cliente.

- DDL Tabla clientes:
~~~
    CREATE TABLE clientes (
	cliente_id INT PRIMARY KEY,
	nombre VARCHAR,
	email VARCHAR
   );
~~~
~~~
  SELECT alquiler.fecha_renta, pelicula.titulo, pelicula.genero, cliente.nombre
  FROM pelicula
  INNER JOIN alquiler
  ON pelicula.id = alquier.pelicula_id
  INNER JOIN cliente
  ON alquiler.cliente_id = cliente.id
  ORDER BY pelicula.titulo, cliente.nombre, alquiler.fecha_renta DESC;
~~~
- La consulta devolverá cuatro columnas: 'fecha_renta', 'titulo' de la película, 'genero', y 'nombre' del cliente, ordenadas por la fecha de renta más reciente.
- La relación entre 'cliente' y 'alquiler' es de uno a muchos. Esto significa que un cliente puede tener varios alquileres (es decir, 'cliente_id' aparece varias veces en la tabla 'alquiler'), pero cada registro de alquiler está asociado a un solo cliente.

