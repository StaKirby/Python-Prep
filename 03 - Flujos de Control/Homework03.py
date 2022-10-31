# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
a = 10
if a > 0:
    print('Es mayor a 0')
elif a < 0:
    print('Es menor a 0')
else:
    print('Es igual a 0')

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
b = "soy str"
if type(a) == type(b):
    print('a y b son del mismo tipo de dato')
else:
    print('a y b son diferentes tipos de datos')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1, 21):
    if i % 2 == 0:
        print(f'{i} es par')
    else:
        print(f'{i} es impar')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(6):
    print(f'{i} al cubo =', i**3)

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
rango = 10
for i in range(rango):
    print(f'Este ciclo se repetira {rango} veces.')

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
i = 5
fact = 1
if type(i) == int:
    if i > 0:
        num = i
        while i > 0:
            fact *= i
            i -= 1
        print(f'El factorial de {num} es {fact}')
    elif i == 0:
        print('El factorial de 0 es 1')
    else:
        print('Esta intentando el factorial de un numero negativo...')
else:
    print(f'{i} no es un numero entero.')

# 7) Crear un ciclo for dentro de un ciclo while
vueltawhile = 0
vueltafor = 0
while vueltawhile < 5:
    vueltawhile += 1
    for i in range(vueltawhile):
        vueltafor += 1
        print(f'While: {vueltawhile} vueltas. For: {vueltafor} vueltas.')        

# 8) Crear un ciclo while dentro de un ciclo for
vueltawhile = 0
vueltafor = 0
for i in range(5):
    vueltafor +=1
    while i < 5:
        vueltawhile += 1
        print(f'While: {vueltawhile} vueltas. For: {vueltafor} vueltas.')
        break

# 9) Imprimir los números primos existentes entre 0 y 30
print('2')
for i in range(3, 31, 2):
    flag_primo = True

    for div in range(2, i):
        if i % div == 0:
            flag_primo = False
    
    if flag_primo:
        print(i)
      
    flag_primo = True    

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
print('2')
cant_pri = 0
for i in range(3, 31, 2):
    flag_primo = True

    for div in range(2, i):
        if i % div == 0:
            cant_pri += 1
            flag_primo = False
            break
    
    if flag_primo:
        print(i)
      
    flag_primo = True 

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
print('2')
cant_pri = 0
for i in range(3, 31, 2):
    flag_primo = True

    for div in range(2, i): # SI AYUDA EL BREAKE
        if i % div == 0:
            cant_pri += 1
            flag_primo = False
            break
    
    if flag_primo:
        print(i)
      
    flag_primo = True 
print(cant_pri)

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print('2')
cant_pri = 0
for i in range(3, 100, 2): # SI CRECE   
    flag_primo = True

    for div in range(2, i):
        if i % div == 0:
            cant_pri += 1
            flag_primo = False
            break
    
    if flag_primo:
        print(i)
      
    flag_primo = True 
print(cant_pri)

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
num = 100
while num <= 300:
    num += 1
    if num % 12 != 0:
        continue
    print(f'{num} es divisible por 12.')

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
print('2')
cant_pri = 1

primos = int(input('Ingrese la cantidad de numeros a analizar: '))

for i in range(3, primos, 2):
    flag_primo = True

    for div in range(2, i):
        if i % div == 0:
            flag_primo = False
            break
    
    if flag_primo:
        cant_pri += 1
        print(i)
    flag_primo = True 
print(cant_pri)

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
num = 200
while num <= 300:
    num += 1
    if num % 6 == 0:
        print(f'{num} Es divisible por 3 y multiplo de 6')
        break
