import unittest

class TestExample(unittest.TestCase):

    def test_suma(self):
        num1 = 3
        num2 = 4
        resultado = num1 + num2

        #7
        #assert resultado == 7

        self.assertEqual(resultado, 7)
    
    def test_resta(self):
        self.assertEqual(100-50, 50)

if __name__ == '__main__':
    unittest.main()