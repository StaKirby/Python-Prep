#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
from cmath import pi


variable1 = 1
print('1):', variable1)

#2) Imprimir el tipo de dato de la constante 8.5
variable2 = 8.5
print('2):', type(variable2))

#3) Imprimir el tipo de dato de la variable creada en el punto 1
print('3):', type(variable1))

#4) Crear una variable que contenga tu nombre
variable3 = "Facu"

#5) Crear una variable que contenga un número complejo
variable4 = 1 + 1j

#6) Mostrar el tipo de dato de la variable crada en el punto 5
print('6):', type(variable4))

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
variable5 = round(pi, 4)

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable6 = 'True'
variable7 = True

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print('8) Variable6:', type(variable6), 'Variable7:', type(variable7))

#10) Asignar a una variable, la suma de un número entero y otro decimal
variable8 = 10 + 10.5

#11) Realizar una operación de suma de números complejos
variable9 = variable4 + (2+5j)

#12) Realizar una operación de suma de un número real y otro complejo
variable10 = -3.5 + variable9

#13) Realizar una operación de multiplicación
variable11 = 2 * 4

#14) Mostrar el resultado de elevar 2 a la octava potencia
print('14):', 2 ** 8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
variable12 = 27 / 4
print('15):', variable11)

#16) De la división anterior solamente mostrar la parte entera
variable13 = 27 // 4

#17) De la división de 27 entre 4 mostrar solamente el resto
variable14 = 27 % 4

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
variable15 = variable13 * 4 + variable14
print('18):', variable15)

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print('19):', 'Hello' + ' World')

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
variable16 = '2' == 2
print('20)', variable16)

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
variable17 = int('2') == 2
print('21):', variable17)

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# SE USA "." NO ","

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
variable18 = 3
variable18 -= 1
print('23):', variable18)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print('24):', 1 << 2)

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# NO PODES SUMAR NUMEROS ENTEROS CON CADENAS DE CARACTERES (INTENTA SUMAR 2 + HOLA)

#26) Realizar una operación válida entre valores de tipo entero y string
print(5 * 'ja ')