# archivo: test_calculator.py
import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        # Configurar Flask para realizar pruebas
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        # Probar la suma
        response = self.app.post('/calculate', data=dict(num1=5, num2=3, operation='add'))
        self.assertIn(b'8.0', response.data)

    def test_subtraction(self):
        # Probar la resta
        response = self.app.post('/calculate', data=dict(num1=5, num2=3, operation='subtract'))
        self.assertIn(b'2.0', response.data)

    def test_multiplication(self):
        # Probar la multiplicación
        response = self.app.post('/calculate', data=dict(num1=5, num2=3, operation='multiply'))
        self.assertIn(b'15.0', response.data)

    def test_division(self):
        # Probar la división
        response = self.app.post('/calculate', data=dict(num1=6, num2=3, operation='divide'))
        self.assertIn(b'2.0', response.data)

if __name__ == '__main__':
    unittest.main()
