# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor
class vehiculo:
    def __init__(self, color, tipo, motor):
        self.color = color
        self.tipo = tipo
        self.motor = motor
        
# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>
class vehiculo:
    def __init__(self, color, tipo, motor):
        self.color = color
        self.tipo = tipo
        self.motor = motor
        self.velocidad = 0
        self.grados = 0
    
    def acelerar(self, acel):
        self.velocidad += acel

    def frenar(self, fren):
        self.velocidad -= fren

    def doblar(self, grados):
        self.grados += grados


# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
veh1 = vehiculo("Negro", "Moto", 2)
veh2 = vehiculo("Blanco", "Camioneta", 4)
veh3 = vehiculo("Negro", "Camion", 6)

veh1.acelerar(80)
veh1.frenar(20)
veh1.doblar(45)
veh2.acelerar(60)
veh2.frenar(10)
veh2.doblar(20)
veh3.acelerar(100)
veh3.frenar(30)
veh3.doblar(25)

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada
class vehiculo:
    def __init__(self, color, tipo, motor):
        self.color = color
        self.tipo = tipo
        self.motor = motor
        self.velocidad = 0
        self.grados = 0
    
    def acelerar(self, acel):
        self.velocidad += acel

    def frenar(self, fren):
        self.velocidad -= fren

    def doblar(self, grados):
        self.grados += grados
    
    def estado(self):
        print(f"Tengo una velocidad de {self.velocidad}km/h y una direccion de {self.grados}°.")
    
    def soy(self):
        print(f"Soy tipo {self.tipo} de color {self.color} y una cilindrada de {self.motor}")

veh1 = vehiculo("Negro", "Moto", 2)
veh2 = vehiculo("Blanco", "Camioneta", 4)
veh3 = vehiculo("Negro", "Camion", 6)

veh1.acelerar(80)
veh1.frenar(20)
veh1.doblar(45)
veh2.acelerar(60)
veh2.frenar(10)
veh2.doblar(20)
veh3.acelerar(100)
veh3.frenar(30)

veh1.estado()

# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>
class modulo6:
    def __init__(self) -> None:
        pass

    def esprimo(num):
        if num == 2:
            return True
        elif num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(num/2), 2):
            if num % i == 0:
                return False
        return True
    
    def modal(lis = [], mayor = True):
        first_flag = True
        mod = ""
        if mayor:
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

    def factorial(self, num):
        if type(num) != int or num < 0:
            return
        elif num == 0:
            return 1
        elif num > 1:    
            num *= self.factorial(num - 1)
        return num

# 6) Probar las funciones incorporadas en la clase del punto 5
print(modulo6.esprimo(2))
print(modulo6.modal([1,1,1,3,3,3], False))
print(modulo6.conv_grad(1, "farenheit", "celsius"))
x = modulo6()
print(x.factorial(5))

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se apliquen las funciones incorporadas
class modulo6:
    def __init__(self, lis):
        self.lis = lis

    def esprimo(self):
        for i in self.lis:
            if self._esprimo(i):
                print(f"{i} es primo")
            else:
                print(f"{i} no es primo")
    
    def conv_grad(self, origen, destino):
        for i in self.lis:
            print(f"{i, origen} = {self._conv_grad(i, origen, destino), destino}")

    def factorial(self):
        for i in self.lis:
            print(f"Factorial de {i}: {self._factorial(i)}")

    def modal(self, mayor = True):
        first_flag = True
        if mayor:
            self.lis.sort(reverse = True)
        else:
            self.lis.sort()
    
        for i in self.lis:
            cant = self.lis.count(i)
            if first_flag:
                mod = [i, cant]
                first_flag = False
            elif cant > mod[1]:
                mod = [i, cant]
        return mod

    def _esprimo(self, num):
        if num == 2:
            return True
        elif num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(num/2), 2):
            if num % i == 0:
                return False
        return True
    

    def _conv_grad(self, valor, origen, destino):
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

    def _factorial(self, num):
        if type(num) != int or num < 0:
            return
        elif num == 0:
            return 1
        elif num > 1:    
            num *= self._factorial(num - 1)
        return num

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
from Homework07Herr import *

x = herramienta07([1,2,3,4,5,6,7,8,9,10,11])
x.factorial()