import unittest

from lib import factorial, sum, hex_to_rgb

class CWTestCase(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(1), 1)
    
    def test_sum(self):
        self.assertEqual(sum(5), 15)
        self.assertEqual(sum(10), 55)
        self.assertEqual(sum(1), 1)
    
    def test_hex_to_rgb(self):
        self.assertEqual(hex_to_rgb('2d2d2d'), (45, 45, 45))
        self.assertEqual(hex_to_rgb('011926'), (1, 25, 38))
        self.assertEqual(hex_to_rgb('ffb80b'), (255, 184, 11))

if __name__ == '__main__':
    unittest.main()
