import unittest

from lib import factorial, sum

class CWTestCase(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(1), 1)
    
    def test_sum(self):
        self.assertEqual(sum(5), 15)
        self.assertEqual(sum(10), 55)
        self.assertEqual(sum(1), 1)

if __name__ == '__main__':
    unittest.main()
