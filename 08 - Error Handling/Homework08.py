# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. 
# Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?
import Homework07Herr
x = Homework07Herr.herramienta07([2,3,5,6,2])

# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.
print(x.conv_grad('celsius','farenheit'))

# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.
import unittest
class pruebas(unittest.TestCase):

    def test_obj_inc(self):
        parametro = "hola"
        self.assertRaises(ValueError, Homework07Herr.herramienta07, parametro)

    def test_obj(self):
        parametro = [1,2,3]
        x = Homework07Herr.herramienta07(parametro)
        self.assertEqual(x.lis, parametro)

    def test_modal(self):
        parametro = [1,1,2,3]
        res_esperado = [1,2]
        x = Homework07Herr.herramienta07(parametro)
        res = x.modal()
        self.assertEqual(res, res_esperado)

unittest.main(argv=[''], verbosity=2, exit=False)

# 4) Probar una creación incorrecta y visualizar la salida del "raise"
'''x = Homework07Herr.herramienta07("mal")'''

# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función 
# de que el elemento en la posisicón sea o no primo
class pruebas2(unittest.TestCase):

    def test_primos(self):
        parametro = [2,3,5,6]
        res_esperado = [True, True, True, False]
        x = Homework07Herr.herramienta07(parametro)
        res = x.esprimo()
        self.assertEqual(res, res_esperado)

unittest.main(argv=[''], verbosity=2, exit=False)

# 7) Agregar casos de pruebas para el método conversion_grados()
class pruebas3(unittest.TestCase):

    def test_grados(self):
        parametro = [2,3,5,6,2]
        res_esperados = [35.6, 37.4, 41.0, 42.8, 35.6]
        x = Homework07Herr.herramienta07(parametro)
        res = x.conv_grad('celsius','farenheit')
        self.assertEqual(res, res_esperados)

unittest.main(argv=[''], verbosity=2, exit=False)

# 8) Agregar casos de pruebas para el método factorial()
class pruebas4(unittest.TestCase):

    def test_factorial(self):
        parametro = [1,2,3]
        res_esperados = [1, 2, 6]
        x = Homework07Herr.herramienta07(parametro)
        res = x.factorial()
        self.assertEqual(res, res_esperados)

unittest.main(argv=[''], verbosity=2, exit=False)

# 9) Completar el código en las funciones del archivo "checkpoint.py" y probarlo a partir de la ejecución del script "tests.py"