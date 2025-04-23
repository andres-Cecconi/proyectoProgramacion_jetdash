## Introducción

El presente documento tiene como finalidad describir los aspectos fundamentales del proyecto académico **JetDash**, un videojuego de desplazamiento lateral desarrollado en Python mediante el uso de la biblioteca Pygame. Su propósito es definir el alcance del producto, establecer los objetivos y metas, detallar los requisitos funcionales y no funcionales, y organizar los entregables conforme a las etapas de avance previstas. Esta propuesta busca integrar de forma aplicada los conceptos trabajados durante la cursada, promoviendo el desarrollo de competencias en programación estructurada, diseño modular y resolución de problemas.

## Alcance del Proyecto
*Propósito General:*
Desarrollar un videojuego de tipo endless runner que permita aplicar conocimientos de programación en un entorno visual e interactivo, utilizando estructuras de datos, funciones modulares y lógica de eventos.

*Beneficios Esperados:*
- Contribuir al desarrollo de habilidades lógico-computacionales mediante un entorno lúdico, promoviendo el aprendizaje  significativo a través de la acción.
- Fomentar la creatividad y la resolución de problemas aplicando conceptos fundamentales de programación estructurada en un proyecto con impacto visual.
- Ofrecer una experiencia interactiva que simula escenarios dinámicos y desafía la capacidad de respuesta del jugador, incentivando la concentración y el pensamiento estratégico.
- Potenciar la motivación intrínseca del grupo al generar un producto final atractivo, exportable y replicable.
- Establecer una base para futuros desarrollos más complejos, fortaleciendo la comprensión del ciclo completo de desarrollo de software en entornos gráficos.

*Objetivos Específicos:*
- Construir un juego funcional, con interacción continua entre el jugador y el entorno.
- Implementar la lógica de colisiones, generación aleatoria de obstáculos y progresión de dificultad.
- Utilizar técnicas de programación estructurada y principios de desarrollo mantenible.
- Generar una experiencia de usuario fluida y visualmente clara.

*Metas del Proyecto:*
- Alcanzar una versión inicial funcional que permita demostrar la mecánica de juego básica en la primera entrega (40%).
- Incorporar mejoras visuales, interfaz de usuario, efectos sonoros y ajustes dinámicos de dificultad para la segunda entrega (80%).
- Consolidar una versión final optimizada, documentada y modularizada con todos los requisitos cumplidos, para la entrega completa (100%).

## Requisitos Funcionales
El jugador controlará un personaje que se desplaza automáticamente hacia la derecha.
Mediante la interacción con una tecla, podrá impulsarse hacia arriba (mecánica de jetpack).
El fondo del escenario se desplazará horizontalmente para simular avance.
Se generarán obstáculos de forma aleatoria que deberán ser evitados.
El sistema detectará colisiones entre el personaje y los obstáculos, finalizando la partida si ocurre un impacto.
El juego mostrará un puntaje que aumentará con el tiempo de supervivencia.
Existirán pantallas de inicio, juego y fin, con posibilidad de reiniciar.
El código será organizado en módulos separados para facilitar su mantenimiento.

## Requisitos No Funcionales
El código debe cumplir con principios de claridad, simplicidad y reutilización.
Se empleará documentación mediante docstrings en todas las funciones.
La experiencia de usuario debe ser fluida, sin interrupciones perceptibles.
Se priorizará el correcto funcionamiento del juego en distintos dispositivos con Python instalado.

## Entregables
**Entrega 40% -- Funcionalidad Mínima Viable** 
En esta etapa se entregará un prototipo jugable que demuestre la mecánica principal y la integración básica de módulos:

📌 Pantalla de menú principal, con opciones de "jugar", "configuracion" y "salir", usando fuente retro. 
📌 Sub-menú de Configuración (activar/desactivar música y efectos), integrando audio dinámico.
📌 Control de vuelo básico: ascenso al mantener pulsada la tecla y descenso por gravedad.
📌 Scroll de fondo en bucle para simular avance lateral.
📌 Generación y desplazamiento de obstáculos sencillos (misiles estáticos o en línea), usando estructuras de datos (listas, tuplas).
📌 Sistema de puntuación en pantalla que cuenta el tiempo de supervivencia.
📌 Gestión de eventos y uso de funciones lambda para parámetros sencillos (por ejemplo velocidad base).

**Entrega 80% -- Funcionalidades Avanzadas**
Se ampliarán las capacidades del prototipo con elementos visuales y lógicos adicionales, mejorando la jugabilidad:

📌 Detección de colisiones completa y pantalla de Game Over.
📌 Mejora estética: sprites personalizados, animaciones básicas.
📌 Dificultad progresiva: aumento de velocidad y frecuencia de obstáculos mediante funciones lambda.
📌 Power-ups básicos (por ejemplo, escudo temporal o multiplicador de puntuación).
📌 Persistencia simple del puntaje con lista/ranking local.
📌 Interfaz de usuario mejorada: pantallas de inicio, pausa y fin con navegación.
📌 Documentación parcial con docstrings y comentarios en módulos clave

**Entrega 100% -- Versión Final**
En la entrega final se completará el proyecto con refinamientos, optimización y cumplimiento total de requisitos:

📌 Refinamiento gráfico: parallax, partículas de explosión y transiciones suaves.
📌 Optimización del rendimiento del juego.
📌 Documentación con docstrings completa de todas las funciones y clases.
📌 Integración de niveles: múltiples fondos o escenarios desbloqueables
📌 Presentación final con demostración funcional del producto (video o sesión en vivo).

