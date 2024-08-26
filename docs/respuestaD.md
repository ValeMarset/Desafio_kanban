### Pregunta:

>¿A qué hace referencia el Patrón de Arquitectura de Diseño de Software conocido como Modelo Vista Controlador (MVC)? ¿Cuál es su utilidad?

- **El Patrón de Arquitectura MVC (Modelo Vista Controlador)** es una estructura utilizada para organizar y separar las responsabilidades dentro de una aplicación en tres componentes principales: Modelo, Vista y Controlador.

  - **Modelo**: Es responsable de la lógica del negocio y la gestión de datos. Se encarga de manipular, gestionar y actualizar la información de una base de datos o cualquier otra fuente de datos.

  - **Vista**: Es el componente que presenta los datos del Modelo al usuario de forma visual. Su función es mostrar la información, pero no contiene lógica sobre cómo se procesan esos datos.

  - **Controlador**: Actúa como intermediario entre la Vista y el Modelo. Recibe las entradas del usuario, las procesa, y actualiza el Modelo según sea necesario. Luego, solicita al Modelo los datos actualizados para que la Vista los muestre al usuario.

Los tres componentes de MVC están conectados a través del Controlador. La Vista muestra la información que recibe del Controlador, quien se encarga de gestionar las interacciones del usuario. El Controlador procesa las entradas del usuario, actualiza el Modelo y luego actualiza la Vista con los nuevos datos del Modelo, manteniendo la aplicación organizada y modular.
