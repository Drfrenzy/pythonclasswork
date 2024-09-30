import unittest
from multiplication import multiplication  

class TestMultiplicationFunction(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(5, 6), 30)
    
    def test_multiplication_floats(self):
        self.assertAlmostEqual(multiplication(5.5, 4), 22.0)
    
    def test_multiplication_negative_numbers(self):
        self.assertEqual(multiplication(-5, 4), -20)
        self.assertEqual(multiplication(5, -4), -20)
        self.assertEqual(multiplication(-5, -4), 20)
    
    def test_multiplication_zero(self):
        self.assertEqual(multiplication(0, 9), 0)
        self.assertEqual(multiplication(8, 0), 0)
    
    def test_multiplication_integer_and_float(self):
        self.assertAlmostEqual(multiplication(5, 2.5), 12.5)
    
    def test_multiplication_large_numbers(self):
        self.assertEqual(multiplication(2323, 3245), 7538135)

if __name__ == '__main__':
    unittest.main()
