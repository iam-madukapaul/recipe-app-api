"""Sample tests"""
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test adding numbers together."""
    def test_add_numbers(self):
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
    
    
    """Test subtract numbers."""   
    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        
        self.assertEqual(res, 5)

    