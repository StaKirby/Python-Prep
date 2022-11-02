# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
negativos = []
negativo = -1

while negativo >= -15:
    negativos.append(negativo)
    negativo -= 1
print(negativos)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
i = 0
pares_while = []

while i < len(negativos):
    if negativos[i] % 2 == 0:
        pares_while.append(negativos[i])
    i += 1
print(pares_while)

# 3) Resolver el punto anterior sin utilizar un ciclo while
pares_for = [i for i in negativos if i % 2 == 0]

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

for i in negativos[:3]:
    print(i)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
for i, j in enumerate(negativos[:3]):
    print(i, j)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
lista = [1,2,5,7,8,10,13,14,15,17,20]

for i in range(1, lista.pop() + 1):
    if not i in lista:
        lista.insert(i - 1, i)
        print(f"se inserto el {i}")

print(lista)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>
fibo = [0, 1]
cant = 30

for i in range(2, cant):
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo)
# 8) Realizar la suma de todos elementos de la lista del punto anterior
print(sum(fibo))

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo.
#  El cuál se puede aproximar con la sucesión de Fibonacci.
#  Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub>< br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
aureo = []
rango_fin = len(fibo)

for i in range(rango_fin - 5, rango_fin):
    aureo.append(fibo[i]/fibo[i-1])
print(aureo)

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i, j in enumerate(cadena):
    if j in "nN":
        print(i)

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador
diccionario = {"Ciudad": ["Cordoba", "Roma", "Paris"], 
"Gaston": ["AOE2", "CS1.6", "Terraria"], 
"Facu": ["PES", "Wow", "CSGO"]}

for i in diccionario:
    print(i)

# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
cadena2 = list(cadena)

for i in cadena2:
    print(i)

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip
lista1 = [1, 2, 3, 4]
lista2 = ["uno", "dos", "tres", "cuatro"]

tupla = tuple(zip(lista1, lista2))
print(tupla)

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
div_7 = [i for i in lis if i % 7 == 0]
print(div_7)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lis2 = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
elementos = 0

for i in lis2:
    if type(i) == list:
        elementos += len(i)
    else:
        elementos += 1
print(elementos)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
for i, j in enumerate(lis2):
    if type(j) != list:
        lis2[i] = [j]
print(lis2)