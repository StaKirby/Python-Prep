# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def esprimo(num):
    if num == 2:
        return True
    elif num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num/2), 2):
        if num % i == 0:
            return False
    return True
# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
def esprimo_lis(lis):
    primos = []
    for num in lis:
        flag_primo = True
        if num == 2:
            primos.append(num)
            continue
        elif num < 2 or num % 2 == 0:
            continue
        for i in range(3, int(num/2), 2):
            if num % i == 0:
                flag_primo = False
                break 
        if flag_primo:
            primos.append(num)
        
    return primos

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
def mayrepe_lis(lis = []):
    first_flag = True
    may = ""

    for i in lis:
        cant = lis.count(i)
        if first_flag:
            may = [i, cant]
            first_flag = False
        elif cant > may[1]:
            may = [i, cant]
    return may

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
def modal(lis = [], mayor = True):
    first_flag = True
    mod = ""
    if not mayor:
        lis.sort(reverse = True)
    else:
        lis.sort()

    for i in lis:
        cant = lis.count(i)
        if first_flag:
            mod = [i, cant]
            first_flag = False
        elif cant > mod[1]:
            mod = [i, cant]
    return mod

print(modal([10,1,5,6,8,10,22,5,6,4,11,10,9,5]))

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
def conv_grad(valor, origen, destino):
    origen, destino = origen.lower(), destino.lower()
    if origen == "celsius":
        if destino == "farenheit":
            val_mod = (valor * 9/5) + 32
        elif destino == "kelvin":
            val_mod = valor + 273.15
        else:
            val_mod = valor
    elif origen == "farenheit":
        if destino == "celsius":
            val_mod = (valor - 32) / (9/5)
        elif destino == "kelvin":
            val_mod = ((valor - 32) / (9/5)) + 273.15
        else:
            val_mod = valor
    else:
        if destino == "celsius":
            val_mod = valor - 273.15
        elif destino == "farenheit":
            val_mod = ((valor - 273.15) * 9/5) + 32
        else:
            val_mod = valor
    return val_mod

# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
metricas = ['celsius','kelvin','farenheit']
for i in range(3):
    for j in range(3):
        print(f"1 grado {metricas[i]} a {metricas[j]}: {conv_grad(1, metricas[i], metricas[j])}")

# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
def factorial(num):
    if type(num) != int or num < 0:
        return
    elif num == 0:
        return 1
    elif num > 1:    
        num *= factorial(num - 1)
    return num
