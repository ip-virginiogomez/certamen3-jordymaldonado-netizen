[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vuK1zRkc)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=24137496)
# Certamen 3

Este trabajo es individual. El objetivo es que apliques estructuras de control, lógica y manejo de datos básicos en Python, resolviendo situaciones similares a las que podrías enfrentar en la vida real.

## Objetivos
- Aplicar estructuras de control y lógica en Python.
- Manejar datos básicos como listas y matrices.
- Aplicar conocimientos en control de versiones y buenas prácticas de programación.
- Desarrollar habilidades de resolución de problemas mediante programación.

## Información General
- Duración: 80 minutos.
- Puntaje total: 80 puntos.

## Instrucciones Generales
- Debes resolver los problemas utilizando Python.
- Cada problema tiene un puntaje asignado y criterios de evaluación específicos.
- No debes usar librerías externas ni funciones avanzadas.
- Entrega tu código en un archivo `.py` por cada problema.
- Asegúrate de que tu código sea claro, ordenado y bien comentado.

---

## Problema 1: Control de Velocidad en una Autopista (25 pts)

**Enunciado:**
Una autopista instaló sensores para registrar la velocidad de los vehículos y detectar infracciones. Debes crear un programa que analice los registros y emita alertas cuando corresponda.

**Indicaciones paso a paso:**
1. Solicita al usuario que ingrese 5 velocidades (en km/h).
2. Guarda las velocidades en una lista.
3. Calcula el promedio y la velocidad máxima registrada.
4. Verifica si todas las velocidades están dentro del límite permitido (entre 60 y 120 km/h).
5. Si alguna velocidad supera los 140 km/h o es menor a 20 km/h, muestra una advertencia de peligro.

**Puntos asignados:** 25 pts

**Criterios evaluados:**
- Uso correcto de lista y cálculos (10 pts)
- Evaluación de condiciones lógicas (10 pts)
- Orden y claridad del código (5 pts)

---

## Problema 2: Registro de Ventas de una Tienda (35 pts)

**Enunciado:**
Una pequeña tienda registra las ventas diarias de 3 vendedores durante 3 días de la semana. El dueño quiere saber el rendimiento de cada vendedor y si alguno tuvo bajo desempeño.

**Indicaciones paso a paso:**
1. Crea una matriz 3x3 para guardar los montos de ventas (cada fila es un vendedor, cada columna es un día).
2. Calcula el total de ventas de cada vendedor (suma por fila solamente).
3. Identifica qué vendedor tuvo el mayor total de ventas.
4. Muestra una alerta si el total de algún vendedor es menor a $30.000.

**Puntos asignados:** 35 pts

**Criterios evaluados:**
- Representación correcta de la matriz (10 pts)
- Cálculo correcto del total por vendedor (10 pts)
- Identificación del mejor vendedor (10 pts)
- Claridad en mensajes y formato (5 pts)

---

## Problema 3: Sistema de Descuento en Supermercado (20 pts)

**Enunciado:**
Un supermercado aplica descuentos especiales a sus clientes. Para acceder al descuento, el cliente debe ser mayor de 60 años o tener una tarjeta de socio, y además el total de su compra debe superar los $10.000.

**Indicaciones paso a paso:**
1. Solicita al usuario su edad, si tiene tarjeta de socio (sí/no) y el monto total de su compra.
2. Verifica si cumple las condiciones: el monto debe superar $10.000 y debe ser mayor de 60 años o tener tarjeta de socio.
3. Muestra un mensaje indicando si obtiene el descuento del 15% o si no califica, mostrando el monto final en cada caso.

**Puntos asignados:** 20 pts

**Criterios evaluados:**
- Uso correcto de operadores lógicos (10 pts)
- Validación de condiciones y entrada de datos (5 pts)
- Claridad de la salida (5 pts)
