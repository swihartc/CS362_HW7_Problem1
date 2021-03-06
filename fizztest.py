import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def testFizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(10),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(15),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(20),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(25),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(26),None)
        self.assertEqual(fizzbuzz.fizzbuzz(24),None)

if __name__ == '__main__':
    unittest.main()