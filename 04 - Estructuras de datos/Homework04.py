# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
ciudades = ["Cordoba", "Roma", "Paris", "Madrid", "New York", "Ciudad de Mexico"]
print(ciudades)

# 2) Imprimir por pantalla el segundo elemento de la lista
print(ciudades[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:4])

# 4) Visualizar el tipo de dato de la lista
print(type(ciudades))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(ciudades[2:])

# 6) Visualizar los primeros 4 elementos de la lista
print(ciudades[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades.append("Paris")
ciudades.append("Tokio")
print(ciudades)

# 8) Agregar otra ciudad, pero en la cuarta posición
ciudades.insert(3, "Cordoba")
print(ciudades)

# 9) Concatenar otra lista a la ya creada
ciudades.extend([1, 2, 3])
print(ciudades)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(ciudades.index("Paris"))
'''solo te muestra el indice del primer valor que encuentra en la lista'''

# 11) ¿Qué pasa si se busca un elemento que no existe?
'''Error de interprete'''
# print(ciudades.index("Santiago"))


# 12) Eliminar un elemento de la lista
ciudades.remove("Paris")
print(ciudades)

# 13) ¿Qué pasa si el elemento a eliminar no existe?
'''Error de interprete'''
#ciudades.remove("Santiago")

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
ultimo = ciudades.pop()
print(ultimo)

# 15) Mostrar la lista multiplicada por 4
print(ciudades * 4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20
numeros = tuple(range(1, 21))
print(numeros)

# 17) Imprimir desde el índice 10 al 15 de la tupla
print(numeros[10:15])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla
if 20 in numeros:
    print("El 20 esta en la tupla")
else:
    print("El 20 no esta en la tupla")

if 30 in numeros:
    print("El 30 esta en la tupla")
else:
    print("El 30 no esta en la tupla")

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
elemento = "Londres"
if elemento in ciudades:
    print(f"{elemento} ya se encontraba dentro de la lista.")
else:
    ciudades.append(elemento)
    print(f"{elemento} no se encontraba dentro de la lista, se agrego al final.\n", ciudades)

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(ciudades.count("Roma"))
print(numeros.count(4))

# 21) Convertir la tupla en una lista
numeros2 = list(numeros)
print(type(numeros2))

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
uno, dos, tres, *_= numeros
print(uno, dos, tres)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
diccionario = {"Ciudad": ciudades, 
"Gaston": ["AOE2", "CS1.6", "Terraria"], 
"Facu": ["PES", "Wow", "CSGO"]}

# 24) Imprimir las claves del diccionario
print(diccionario["gaston"])

# 25) Imprimir las ciudades a través de su clave
print(diccionario["ciudad"])