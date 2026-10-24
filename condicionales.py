#EJERCICIO 1: CONTROL DE ACCESO
#Solicite al usuario su edad y si posee documento de identidad (S/N).
#Permitir el ingreso únicamente si:
#Tiene 18 años o más.
#Posee documento de identidad.
#En caso contrario, informar el motivo por el cual no puede ingresar.
"""edad = int(input('Favor ingrese su edad: '))
d_identidad = input('Cuenta con documento de identidad? (SI/NO) ')
if edad >= 18 and d_identidad == 'SI':
    print('Bienvenido, Puede acceder!')
else: 
    print('Lo siento, No puede ingresar!')
    if edad < 18:
        print('Motivo: Es menos de 18 años')
    if d_identidad == 'NO':
        print('Motivo: No cuenta con documento de identidad')"""


#EJERCICIO 2: DESCUENTO EN UNA TIENDA
#Solicite el monto de una compra. Aplicar los siguientes descuentos:
#20% si supera Gs. 500.000
#10% si supera Gs. 200.000
# Sin descuento en cualquier otro caso
#Mostrar: 
# Monto original
# Descuento aplicado
# Total a pagar
"""monto = float(input('Favor ingrese el monto total a abonar: '))

if monto > 500000:
    descuento = monto * 0.20
elif monto > 200000:
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento

print('Monto total sin descuento:', monto)
print('Descuento aplicado: ', descuento)
print('Total a abonar: ', total)"""

#EJERCICIO 3: SEMAFORO INTELIFENTE
#Solicite el color del semáforo:
# - Verde
#- Amarillo
#- Rojo
#Mostrar la acción correspondiente:
#- Avanzar
#- Reducir velocidad
#- Detenerse
#Si el color ingresado no es válido, mostrar un mensaje de error
"""color = input('Ingrese el color en el que se encuentra el semaforo (Verde, Amarillo, Rojo): ').lower()
if color == "verde":
    print('Avanzar')
elif color == "amarillo":
    print('Reducir Velocidad')
elif color == "rojo":
    print('Detenerse')
else:
    print('El color ingresado no es valido!')"""

#EJERCICIO 4: NIVEL DE BATERIA
#Solicite el porcentaje de batería de un teléfono móvil.
#Mostrar:
#- Crítica (0% a 10%)
#- Baja (11% a 30%)
#- Normal (31% a 80%)
#- Alta (81% a 100%)
#Validar que el porcentaje ingresado sea correcto.
"""bateria = int(input('Ingrese el nivel de bateria: '))
if bateria < 0 or bateria > 100:
    print('El numero ingresado es invalido')  
 
if bateria == 0 or bateria <= 10:
    print('Bateria critica')
elif bateria == 11 or bateria <= 30:
    print('Beteria baja')
elif bateria == 31 or bateria <= 80:
    print('Bateria normal')
elif bateria == 81 or bateria <= 100:
    print('Bateria alta')"""

#EJERCICIO 5: EVALUACION CLIMATICA
#Solicite la temperatura actual.
# Mostrar:
#- Mucho frío (menos de 10°C)
#- Templado (10°C a 24°C)
#- Caluroso (25°C a 34°C)
#- Muy caluroso (35°C o más)
"""temperatura = float(input('Ingrese la temperatura actual: '))
if temperatura < 10: 
    print('Esta haciendo mucho frio')
elif temperatura == 10 or temperatura <= 24:
    print('El clima esta templado')
elif temperatura == 25 or temperatura <= 34:
    print('El clima esta caluroso')
elif temperatura >= 35:
    print('El clima esta muy caluroso')"""