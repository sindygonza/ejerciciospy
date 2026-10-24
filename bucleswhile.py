#EJERCICIO 1: CONTADOR ASCENDENTE
#Solicite un número entero positivo e imprima todos los números desde 1 hasta dicho número
#  utilizando un ciclo while.
"""numero = int(input('Ingrese un numero entero positivo: '))
if numero > 0:
    contador = 1

    while contador <= numero:
        print(contador)
        contador += 1
else:
    print('El numero ingresado no es valido!')"""

#EJERCICIO 2: SUMA ACUMULADA
#Solicite números al usuario y acumule la suma.
#El programa debe finalizar cuando el usuario ingrese el valor 0.
#Al finalizar, mostrar la suma total
"""suma = 0
numero = int(input('Ingrese un numero, Para finalizar ingrese el numero 0 '))
while numero != 0:
    suma = suma + numero 
    numero = int(input('Ingrese un numero, Para finalizar ingrese el numero 0 '))
    
print('La suma total es: ', suma)"""

#Ejercicio 3: VALIDACION DE CONTRASEÑA
#Solicite una contraseña al usuario.
#Mientras la contraseña ingresada sea diferente de:
#python123
#debe volver a solicitarla.
#Cuando la contraseña sea correcta, mostrar:
#Acceso concedido
"""contraseña = input('Ingrese la clave para acceder: ')
while contraseña != 'python123': 
    contraseña = input('Ingrese la clave para acceder: ')

print('Acceso concedido..')"""

#EJERCICIO 4: CONTROL DE ASISTENCIA
#Solicite la cantidad de estudiantes presentes en cada clase.
#El ingreso finalizará cuando el usuario introduzca el valor -1.
#Al finalizar, mostrar:
#- Total de asistencias registradas.
#- Cantidad de clases ingresadas.
#- Promedio de asistencia.
"""asistencia_total = 0
clases = 0
asistencia_clases = int(input('Ingrese la asistencia de esta clase, selecione -1 para finalizar:   '))
while asistencia_clases != -1:
    asistencia_total = asistencia_total + asistencia_clases
    clases = clases + 1

    asistencia_clases = int(input('Ingrese la asistencia de esta clase, selecione -1 para finalizar:   '))
print('Total de asistencias: ', asistencia_total)
print('Total de clases: ', clases)

if clases > 0:
    promedio = asistencia_total / clases
    print('El promedio es: ', promedio)
else:
    print('No se encontraron clases registradas..')"""


#EJERCICIO 5: CAJA REGISTRADORA
#Solicite el precio de los productos comprados.
#El ingreso finalizará cuando el usuario ingrese 0.
#Al finalizar mostrar:
#- Cantidad de productos.
#- Monto total de la compra.
"""cantidad = 0
monto_total = 0
precios = float(input('Ingrese el valor del articulo adquirido: (Ingrese el numero 0 para finalizar) '))
while precios != 0:
    cantidad = cantidad + 1
    monto_total = monto_total + precios

    precios = float(input('Ingrese el valor del articulo adquirido: (Ingrese el numero 0 para finalizar) '))

print('Cantidad de productos adquiridos: ', cantidad)
print('Monto total de la compra: ', monto_total)"""