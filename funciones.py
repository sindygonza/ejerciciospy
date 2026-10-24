#EJERCICIO 1: ESTADISTICAS DE UNA LISTA
#Crear una función llamada:
#python
#estadisticas(numeros)
#que reciba una lista de números y retorne:
#- El valor máximo.
#- El valor mínimo.
#- El promedio.
"""def estadisticas(numeros): 
    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)

    return mayor, menor, promedio

numeros = (10,20,30,40,50,60)

mayor, menor, promedio = estadisticas(numeros)

print('Mayor: ', mayor)
print('Menor: ', menor)
print('Promedio: ', promedio)"""


#EJERCICIO 2: BUSCAR UN ELEMENTO
#Crear una función:
#python
#buscar(lista, valor)
#que reciba una lista y un valor.
#La función debe retornar:
#- True si el valor existe.
#- False si el valor no existe.
"""def buscar(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return True 

    return False 

frutas = ["manzana", "banana", "kiwi", "sandia"]

print(buscar(frutas, 'kiwi'))
print(buscar(frutas, 'naranja'))"""


#EJERCICIO 3: ELIMINAR DUPLICADOS
#Crear una función:
#python
#eliminar_duplicados(lista)
#que reciba una lista y retorne una colección sin elementos repetidos utilizando un conjunto (set).
"""def eliminar_duplicados(lista):
    return set(lista)

frutas = ["banana", "manzana", "uva", "manzana", "uva", "uva"]
resultado = eliminar_duplicados(frutas)
print(resultado)"""

#EJERCICIO 4: FRECUENCIA DE ELEMENTOS
#Crear una función:
#python
#contar_frecuencia(lista)
#que reciba una lista y retorne un diccionario indicando cuántas veces aparece cada elemento.
"""def contar_frecuencia(lista):
    frecuencia = {}

    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1  
    return frecuencia 

frutas = ["banana", "manzana", "uva", "manzana", "uva", "uva"]

resultado = contar_frecuencia(frutas)
print(resultado)"""

#EJERCICIO 5: PROMEDIO DE NOTAS
#Crear una función:
#python
#calcular_promedio(notas)
#que reciba una lista de notas y retorne el promedio.
#Crear también una función:
#python
#estado(promedio)
#que indique:
#- "Aprobado" si el promedio es mayor o igual a 60.
#- "Reprobado" en caso contrario.
"""def calcular_promedio(notas):
    promedio = sum(notas)/len(notas)
    return promedio

def estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

#Programa principal
notas = [70, 80, 90, 60]
promedio = calcular_promedio(notas)
print(f'El promedio del alumno es {promedio}')
print(f'El estado del alumno es ' + estado(promedio))"""


#EJERCICIO 6: AGENDA TELEFONICA
#Utilice un diccionario para almacenar contactos.
#Ejemplo:
#python
#agenda = {
#    "Juan": "098111111",
#    "Ana": "098222222"
#}
#Crear las siguientes funciones:
#python
#agregar_contacto()
#buscar_contacto()
#mostrar_contactos()
#El programa debe mostrar el siguiente menú:
#text
#1. Agregar contacto
#2. Buscar contacto
#3. Mostrar contactos
#4. Salir
"""agenda = {
    "Juan": "098111111",
    "Ana": "098222222"
}
#Funciones
def agregar_contacto():
    nombre = input('Ingrese el nombre: ')
    numero = input('Ingrse el número telefónico: ')

    agenda[nombre] = numero
    print('Contacto agregado correctamente..')

def buscar_contacto():
    nombre = input('Ingrese el nombre a buscar: ')
    if nombre in agenda:
        print(f'Teléfono de {nombre}: {agenda[nombre]}')
    else:
        print('Contacto no encontrado..')

def mostrar_contactos():
    if len(agenda) == 0:
        print('La agenda está vacía..')
    else:
        print('\n --- Contactos ---')
        for nombre, telefono in agenda.items():
            print(f'{nombre}:{telefono}')

#Programa principal
while True:
    print('\n === AGENDA TELEFÓNICA ===')
    print('1. Agregar contacto')
    print('2. Buscar contacto')
    print('3. Mostrar contactos')
    print('4. Salir')

    opcion = input('Seleccione una opción: ')
    #Llama a la función en base a la opción de menú seleccionada
    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        mostrar_contactos()
    elif opcion == '4':
        #Salir del programa
        print('Saliendo del programa...')
        break
    else:
        print('Opción inválida')"""


#EJERCICIO 7: PRODUCTO MAS CARO
#Dada la siguiente lista de tuplas:
#python
#productos = [
#    ("Teclado", 150000),
#    ("Mouse", 80000),
#    ("Monitor", 1200000)
#]
#Crear una función:
#python
#producto_mas_caro(productos)
#que retorne el nombre y precio del producto más caro.
### Salida esperada
#text
#Producto: Monitor
#Precio: 1200000
"""def producto_mas_caro(productos):
    mas_caro = productos[0]

    for producto in productos:
        if producto[1] > mas_caro[1]:
            mas_caro = producto

    return mas_caro


productos = [
    ("Teclado", 150000),
    ("Mouse", 80000),
    ("Monitor", 1200000)
]

nombre, precio = producto_mas_caro(productos)

print("Producto:", nombre)
print("Precio:", precio)"""


#EJERCICIO 8: INVENTARIO DE PRODUCTOS
#Utilizando el siguiente diccionario:
#python
#inventario = {
#    "Teclado": 10,
#    "Mouse": 5,
#    "Monitor": 2
#}
#Crear las siguientes funciones:
#python
#agregar_stock()
#vender_producto()
#consultar_stock()
#El programa debe permitir:
#- Aumentar el stock de un producto.
#- Registrar una venta.
#- Consultar la cantidad disponible.
"""def agregar_stock(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
        print("Stock actualizado correctamente")
    else:
        print("El producto no existe en el inventario")


def vender_producto(inventario, producto, cantidad):
    if producto in inventario:
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print("Venta realizada correctamente")
        else:
            print("Stock insuficiente")
    else:
        print("El producto no existe en el inventario")


def consultar_stock(inventario, producto):
    if producto in inventario:
        print("Stock disponible:", inventario[producto])
    else:
        print("El producto no existe en el inventario")"""


#EJERCICIO 9: RANKING DE ALUMNOS
#Dada la siguiente lista de tuplas:
#python
#alumnos = [
#    ("Juan", 85),
#    ("Ana", 95),
#    ("Pedro", 70)
#]
#Crear funciones para:
#- Obtener el mejor alumno.
#- Obtener el peor alumno.
#- Calcular el promedio general.
### Salida esperada
#text
#Mejor alumno: Ana (95)
#Peor alumno: Pedro (70)
#Promedio general: 83.33
"""alumnos = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]


def mejor_alumno(alumnos):
    mejor = alumnos[0]

    for alumno in alumnos:
        if alumno[1] > mejor[1]:
            mejor = alumno

    return mejor


def peor_alumno(alumnos):
    peor = alumnos[0]

    for alumno in alumnos:
        if alumno[1] < peor[1]:
            peor = alumno

    return peor


def promedio_general(alumnos):
    suma = 0

    for alumno in alumnos:
        suma += alumno[1]

    promedio = suma / len(alumnos)

    return promedio


mejor = mejor_alumno(alumnos)
peor = peor_alumno(alumnos)
promedio = promedio_general(alumnos)

print("Mejor alumno:", mejor[0], "(", mejor[1], ")")
print("Peor alumno:", peor[0], "(", peor[1], ")")
print("Promedio general:", round(promedio, 2))"""


#EJERCICIO 10: SISTEMA DE GESTION DE ESTUDIANTES 
#Utilizando un diccionario:
#python
#estudiantes = {
#    "Juan": [70, 80, 90],
#    "Ana": [100, 95, 90]
#}
#Crear las siguientes funciones:
#python
#agregar_estudiante()
#calcular_promedio()
#mostrar_promedios()
#mejor_estudiante()
#El programa debe mostrar el siguiente menú:
#text
#1. Agregar estudiante
#2. Mostrar promedios
#3. Mostrar mejor estudiante
#4. Salir
## Requisitos
#- Utilizar funciones para cada operación.
#- Utilizar estructuras de datos adecuadas.
#- Evitar la repetición de código.
#- Validar las entradas del usuario cuando sea necesario
"""estudiantes = {
    "Juan": [70, 80, 90],
    "Ana": [100, 95, 90]
}


# 1. Agregar estudiante
def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío")
        return

    if nombre in estudiantes:
        print("El estudiante ya está registrado")
        return

    notas = []

    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1}: "))

                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100")

            except ValueError:
                print("Debe ingresar un número válido")

    estudiantes[nombre] = notas
    print("Estudiante agregado correctamente")


# 2. Calcular promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)


# 3. Mostrar promedios
def mostrar_promedios(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados")
        return

    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        print(nombre, ":", round(promedio, 2))


# 4. Mostrar mejor estudiante
def mejor_estudiante(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados")
        return

    mejor_nombre = ""
    mejor_promedio = -1

    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)

        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_nombre = nombre

    print("Mejor estudiante:", mejor_nombre)
    print("Promedio:", round(mejor_promedio, 2))


# 5. Menú principal
while True:
    print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
    print("1. Agregar estudiante")
    print("2. Mostrar promedios")
    print("3. Mostrar mejor estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante(estudiantes)

    elif opcion == "2":
        mostrar_promedios(estudiantes)

    elif opcion == "3":
        mejor_estudiante(estudiantes)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")"""







