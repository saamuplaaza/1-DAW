import primos
import unittest

class Test_TestNumPrimo(unittest.TestCase):
    def test_numero_menor_igual_1(self):
        numero = 1
        resultado = primos.esPrimo(numero)
        self.assertFalse(resultado)
    
    def  test_numero_primo_false(self):
        numero = 4
        resultado = primos.esPrimo(numero)
        self.assertEqual(False, resultado)
    
    def test_numero_primo_true(self):
        numero = 7
        resultado = primos.esPrimo(numero)
        self.assertTrue(resultado)
        
if __name__ == '__main__':
    unittest.main()