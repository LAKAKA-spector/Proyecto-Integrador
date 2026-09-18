# Sistema de Votación — Proyecto Integrador

Sistema desarrollado en Python para la gestión de votaciones con validaciones de seguridad, control de duplicados, cálculo de porcentajes y registro de historiales.

## Autores y Funciones

- **Samuel Garces Cuervo** (SENA - ADSO)
  - **`registrar_voto()`**: Valida que una cédula no vote dos veces utilizando conjuntos (`set`) y verifica la existencia del candidato.
  - **`ver_resultado()`**: Calcula y muestra en pantalla los resultados totales y los porcentajes de cada candidato.
  - **`reiniciar_votacion()`**: Resetea los contadores y guarda automáticamente un archivo de historial (`historial_votacion.txt`).

## Mejora Adicional

- **`mostrar_ganador()`**: Función añadida para determinar de forma automática e inteligente (usando métodos de agregación) quién es el candidato ganador al finalizar la votación.

## Versionado

- **v1.1**: Versión final estable que incluye todas las funcionalidades integradas, mejoras y control de versiones con Git y Conventional Commits.
