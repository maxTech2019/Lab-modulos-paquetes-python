import unittest
import operaciones

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(operaciones.suma(5, 3), 8)
        self.assertEqual(operaciones.suma(-5, 3), -2)
        self.assertEqual(operaciones.suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(operaciones.resta(5, 3), 2)
        self.assertEqual(operaciones.resta(-5, 3), -8)
        self.assertEqual(operaciones.resta(0, 0), 0)

    def test_multiplicacion(self):
        self.assertEqual(operaciones.multiplicacion(5, 3), 15)
        self.assertEqual(operaciones.multiplicacion(-5, 3), -15)
        self.assertEqual(operaciones.multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(operaciones.division(10, 2), 5)
        self.assertEqual(operaciones.division(-10, 2), -5)
        self.assertEqual(operaciones.division(5, 0), "Error: división por cero")

if __name__ == '__main__':
    unittest.main()
