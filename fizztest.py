import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def testFizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(10),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(15),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(20),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(25),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(26),26)
        self.assertEqual(fizzbuzz.fizzbuzz(24),24)
        self.assertEqual(fizzbuzz.fizzbuzz(1),1)
        self.assertEqual(fizzbuzz.fizzbuzz(2),2)

if __name__ == '__main__':
    unittest.main()