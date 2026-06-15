#EJERCICIO 1
velocidad = []
for i in range(5):
    velocidades = float(input(f"ingrese la velocidad del vehiculo {i+1}: km/h"))
    velocidad.append(velocidades) 
print(velocidad)

promedio = sum(velocidad) / len(velocidad) 
maxima = max(velocidad)
print(f"la velocidad promedio es {promedio} km/h")
print(f"la velocidad maxima es {maxima} km/h")

limite_permitido = True
advertencia = False
for velocidades in velocidad:
    if velocidades < 60 or velocidades > 120:
        limite_permitido = False
    if velocidades < 20 or velocidades > 140:
        advertencia = True
        print("advertencia help get out the way danger peligro de velocidadez")

if limite_permitido:
    print("todas las velocidades estan dentro del limite permitido")
else:
    print("al menos una esta fuera del limite")
if not advertencia:
    print("no hay peligro de velocidades")

#EJERCICIO 2
matriz_ventas = [
    [23000,26000,50000],
    [36000,28000,15000],
    [58000,49000,26000]
]

totales_vendedores = [sum(vendedor) for vendedor in matriz_ventas]
for i, total in enumerate(totales_vendedores, 1):
    print(f"Vendedor {i}: ${total:,}")

print("-" * 40)

max_ventas = max(totales_vendedores)
mejor_vendedor_indice = totales_vendedores.index(max_ventas) +1
print("el vendedor con mayor rendimiento es: ", mejor_vendedor_indice , "con un total de $", max_ventas)

print("-" * 40)

alerta = False
for i, total in enumerate(totales_vendedores, 1):
    if total < 30000:
        print("el vendedor ", i , "tuvo bajo desempeño, total: $", total , "meta:30000")
        alerta = True

if not alerta: 
    print("todos los vendedores superaron la meta")

#EJERCICIO 3

edad = int(input("ingrese su edad: "))
tarjeta_socio = input("Tiene tarjeta de socio? responda s?/no ")
monto_total = float(input("Ingrese el monto total de la compra: "))
descuento = 0.85
if edad > 60 and (tarjeta_socio == "s?" or monto_total >= 10000):
    print("El cliente cumple las condiciones para el descuento, el monto total con descuento es: ", monto_total * descuento)
else:
    print("el cliente no cumple las condiciones para el descuento")
