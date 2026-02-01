import unittest
from my_calculation import Calculation

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calc = Calculation(3,5)
        self.assertEqual(calc.get_sum(), 8)
    
    def test_difference(self):
        calc = Calculation(15,4)
        self.assertEqual(calc.get_difference(), 11)
    
    def test_product(self):
        calc = Calculation(10,4)
        self.assertEqual(calc.get_product(), 40)
    
    def test_quotient(self):
        calc = Calculation(28,4)
        self.assertEqual(calc.get_quotient(), 7)
    
    def test_division_by_zero(self):
        calc = Calculation(20,0)
        with self.assertRaises(ZeroDivisionError):
            calc.get_quotient()

if __name__ == '__main__':
    unittest.main()