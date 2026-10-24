#EJERCICIO 1: CONTADOR ASCENDENTE
#Solicite un número entero positivo e imprima todos los números desde 1 hasta dicho número 
# utilizando un ciclo for.
"""numero = int(input('Ingrese un numero entero positivo: '))
if numero > 0:
    for i in range(1, numero + 1):
        print(i)
else:
    print('Error, el numero ingresado no es valido!')"""

#EJERCICIO 2: SUMA DE NUMEROS NATURALES
#Solicite un número entero positivo N y calcule la suma de todos los números desde 1 hasta N.
"""numero = int(input('Ingrese un numero entero positivo: '))
if numero > 0:
    suma = 0
    for i in range(1, numero + 1):
        suma = suma + i
    print('La suma total es: ', suma)
else: 
    print('Error, el numero ingresado no es valido!')"""

#EJERCICIO 3: TABLA DE MULTIPLICAR
#Solicite un número entero e imprima su tabla de multiplicar del 1 al 10 utilizando un ciclo for.
"""numero = int(input('Ingrese un numero entero: '))
for i in range(1,11):
    resultado = numero * i
    print(numero, 'x', i, '=', resultado)"""

#EJERCICIO 4: CONTADOR DE VOCALES
#Solicite una palabra o frase e indique cuántas vocales contiene utilizando un ciclo for.
"""texto = input('Ingrese un texto: ').lower()
contador = 0
for i in texto: 
    if i in 'aeiou':
        contador = contador + 1

print('La cantidad de vocales es: ', contador)"""

#EJERCICIO 5: TRIANGULO DE ATERISCOS
#Solicite un número entero positivo y genere un triángulo de asteriscos utilizando un ciclo for.
"""numero = int(input('Ingrese un numero entero positivo: '))
if numero > 0:
    for i in range(1, numero + 1):
        print('*' * i)
else:
    print('Error, el numero ingresado no es valido!')"""




