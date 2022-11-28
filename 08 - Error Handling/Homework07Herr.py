class herramienta07:
    def __init__(self, lista):
        if type(lista) != list or len(lista) == 0:
            self.lis = []
            raise ValueError("Se esperaba una lista de numeros enteros.")
        else:
            for i in lista:
                if type(i) != int:
                    self.lis = []
                    raise ValueError("Se esperaba una lista de numeros enteros.")
            self.lis = lista


    def esprimo(self):
        lis_primos = []
        for i in self.lis:
            if self._esprimo(i):
                lis_primos.append(True)
            else:
                lis_primos.append(False)
        return lis_primos


    def conv_grad(self, origen, destino):
        par_esperados = ["celsius", "kelvin", "farenheit"]
        conv_list = []
        if str(origen) not in par_esperados or str(destino) not in par_esperados:
            raise ValueError(f"Los parametros esperados son: {par_esperados}")
        for i in self.lis:
            conv_list.append(self._conv_grad(i, origen, destino))
        return conv_list


    def factorial(self):
        lis_factorial = []
        for i in self.lis:
            lis_factorial.append(self._factorial(i))
        return lis_factorial


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