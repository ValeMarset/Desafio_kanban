## Utilice la siguiente consulta:
~~~
    WITH cte AS (
    SELECT name, first_name, last_name, COUNT(*) c,
    RANK() OVER(PARTITION BY name ORDER BY count(*) DESC) AS rank
    FROM procedure p
    JOIN doctor d
    ON p.doctor_id = d.id
    WHERE score >= (SELECT avg(score)
                  FROM procedure pl
                  WHERE pl.name = p.name)
    GROUP BY name, first_name, last_name
    ) 
    SELECT  name, first_name, last_name
    FROM cte
    WHERE rank = 1;
~~~

que muestra los **mejores médicos** para **cada procedimiento** (los que tienen puntuación 1) para escribir una consulta que, dado un conjunto de productos de inventario registrados en la tabla Productos (product_id, product_name, product_cost, product_stock, …) de un ERP, un conjunto de Clientes (customer_id, customer_name, etc) que compran estos productos periódicamente, quedando las ventas registradas en la tabla Invoice (invoice_id, invoice_date, invoice_product_id, invoice_mount, etc)  devuelva:
* Productos más vendidos en el último mes y a qué clientes en orden a su volumen de compra,
* Monto de ventas por cliente de mayor ranking.

#### Respuesta:
~~~
WITH top_sales AS (
    SELECT cliente.customer_name, productos.product_name, SUM(invoice.invoice_mount) AS total_sales
    FROM productos 
    INNER JOIN invoice ON productos.product_id = invoice.invoice_product_id
    INNER JOIN clientes ON invoice.invoice_customer_id = cliente.customer_id
    WHERE invoice.invoice_date >= date_trunc('month', current_date) - INTERVAL '1 month' AND invoice.invoice_date < date_trunc('month', current_date)
    GROUP BY cliente.customer_name, productos.product_name
    ),
ranked_sales AS (
    SELECT customer_name, product_name, total_sales,
           RANK() OVER(PARTITION BY customer_name ORDER BY total_sales DESC) AS rank
    FROM top_sales
)
SELECT customer_name, product_name, total_sales
FROM ranked_sales
WHERE rank = 1
ORDER BY total_sales DESC;

~~~

### Documentación de apoyo utilizada para los desafíos de SQL
Además de guiarme con la anterior consulta, estas fueron algunos de los materiales que consulte:
- [Rank over partition](https://learnsql.com/blog/sql-rank-over-partition/)
- [Obtener fechas de los ultimos meses](https://stackoverflow.com/questions/17461257/getting-all-dates-from-previous-1-month-or-2-months-in-postgresql)
- [Producto más vendido](https://es.stackoverflow.com/questions/382259/como-saber-cual-fue-el-producto-mas-vendido-sql)
- [Cláusula With](https://learnsql.es/blog/que-es-la-clausula-with-en-sql/)

Para abordar el desafío técnico, utilicé inteligencia artificial para formular preguntas disparadoras para alcanzar mi objetivo, estas fueron las preguntas generadas:

- ¿Cómo puedes filtrar las ventas de la tabla Invoice para obtener solo aquellas que ocurrieron en el último mes?
- ¿Qué campo(s) de la tabla Invoice te permitirán calcular el volumen de ventas de cada producto?
- ¿Cómo puedes agrupar los datos para obtener la cantidad total vendida de cada producto en el último mes?
- ¿Cómo puedes relacionar las ventas (de la tabla Invoice) con los clientes que las realizaron (de la tabla Clientes)?
- ¿Qué campo en la tabla Invoice te permitirá identificar qué clientes compraron cada producto?
- ¿Cómo puedes ordenar los productos por el volumen de compra y luego, dentro de cada producto, los clientes por el volumen de sus compras?
- ¿Cómo puedes ordenar los clientes según su ranking de ventas?.
- ¿Cómo vas a combinar todos estos elementos en una sola consulta para que devuelva tanto los productos más vendidos como el monto total de ventas por cliente?
- ¿Cómo se relaciona esta nueva consulta con la estructura de la consulta de ejemplo que te dieron? 

Además, utilicé inteligencia artificial para generar datos de prueba mientras desarrollaba la consulta. A continuación, se muestra el DDL generado:

~~~
-- Tabla de Productos
CREATE TABLE Productos (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_cost DECIMAL(10, 2) NOT NULL,
    product_stock INT NOT NULL
);

-- Datos ficticios para Productos
INSERT INTO Productos (product_name, product_cost, product_stock) VALUES
('Laptop', 1200.00, 50),
('Mouse', 20.00, 150),
('Keyboard', 50.00, 100),
('Monitor', 300.00, 75),
('Printer', 150.00, 40);

-- Tabla de Clientes
CREATE TABLE Clientes (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL
);

-- Datos ficticios para Clientes
INSERT INTO Clientes (customer_name) VALUES
('John Doe'),
('Jane Smith'),
('Alice Johnson'),
('Bob Brown'),
('Charlie Davis');

-- Tabla de Facturas (Invoice)
CREATE TABLE Invoice (
    invoice_id SERIAL PRIMARY KEY,
    invoice_date DATE NOT NULL,
    invoice_product_id INT REFERENCES Productos(product_id),
    customer_id INT REFERENCES Clientes(customer_id),
    invoice_amount INT NOT NULL
);

-- Datos ficticios para Invoice
INSERT INTO Invoice (invoice_date, invoice_product_id, customer_id, invoice_amount) VALUES
('2024-07-20', 1, 1, 3),  -- John Doe compra 3 Laptops
('2024-07-25', 2, 2, 10), -- Jane Smith compra 10 Mouse
('2024-07-26', 3, 3, 5),  -- Alice Johnson compra 5 Keyboard
('2024-07-27', 4, 4, 2),  -- Bob Brown compra 2 Monitors
('2024-07-28', 1, 5, 1),  -- Charlie Davis compra 1 Laptop
('2024-08-01', 2, 1, 15), -- John Doe compra 15 Mouse
('2024-08-02', 3, 2, 7),  -- Jane Smith compra 7 Keyboard
('2024-08-03', 4, 3, 3),  -- Alice Johnson compra 3 Monitors
('2024-08-05', 5, 4, 2),  -- Bob Brown compra 2 Printers
('2024-08-06', 1, 5, 2);  -- Charlie Davis compra 2 Laptops
~~~

### Conclución:
Estas preguntas me ayudaron a orientar mi enfoque y me permitieron desarrollar la consulta con éxito, logrando obtener los resultados propuestos. El DDL generado sirvió como caso de prueba para la consulta, y utilicé PostgreSQL para realizar las pruebas necesarias.


