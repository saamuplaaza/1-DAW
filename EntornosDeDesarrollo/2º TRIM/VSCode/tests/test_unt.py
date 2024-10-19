import inc_dec
import unittest

#clase donde escribimos las pruebas unitarias, se hereda de la clase unittest.TestCase
class Test_TestIncrementoDecremento (unittest.TestCase):
    #cada test o prueba es un método de esta clase. El nombre de cada método debe empezar por test_
    def test_incremento(self):
        self.assertEqual(inc_dec.incremento(3),4)

    def test_decremento(self):
        self.assertEqual(inc_dec.decremento(3), 2)


if __name__ == '__main__': #si este módulo se ejecuta como principal, se ejecutan las pruebas unitarias escritas
    unittest.main()

