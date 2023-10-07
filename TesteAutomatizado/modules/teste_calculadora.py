from Calculadora import Calculadora
import unittest


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        # Criar uma instância da Calculadora antes de cada teste
        self.calc = Calculadora()

    def test_somar(self):
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_subtrair(self):
        resultado = self.calc.subtrair(10, 4)
        self.assertEqual(resultado, 6)

    def test_multiplicar(self):
        resultado = self.calc.multiplicar(6, 2)
        self.assertEqual(resultado, 12)

    def test_dividir(self):
        resultado = self.calc.dividir(8, 4)
        self.assertEqual(resultado, 2)

if __name__ == '__main__':
    unittest.main()
