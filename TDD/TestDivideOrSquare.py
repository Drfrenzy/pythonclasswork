import unittest
import divide_or_square
import math
import cmath

class TestDivideOrSquare(unittest.TestCase):
    def test_divisible_by_5(self):
        self.assertAlmostEqual(divide_or_square.divide_or_square(10), math.sqrt(10))
        self.assertAlmostEqual(divide_or_square.divide_or_square(25), math.sqrt(25))

    def test_not_divisible_by_5(self):
        self.assertEqual(divide_or_square.divide_or_square(7), 2)
        self.assertEqual(divide_or_square.divide_or_square(14), 4)

    def test_negative_numbers(self):
        self.assertEqual(divide_or_square.divide_or_square(-7), 3)
        # self.assertEqual(divide_or_square.divide_or_square(-25), 5) i think you should remove this ... 

# create another function test for it

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            divide_or_square.divide_or_square("string")
        with self.assertRaises(TypeError):
            divide_or_square.divide_or_square(5.5)

if __name__ == '__main__':
    unittest.main()
