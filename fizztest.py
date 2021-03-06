import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def testFizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(6),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(9),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(12),"fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(16),16)
        self.assertEqual(fizzbuzz.fizzbuzz(4),4)
        self.assertEqual(fizzbuzz.fizzbuzz(1),1)
        self.assertEqual(fizzbuzz.fizzbuzz(2),2)
    def testBuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5),"buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(10),"buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(20),"buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(25),"buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(35),"buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(16),16)
        self.assertEqual(fizzbuzz.fizzbuzz(4),4)
        self.assertEqual(fizzbuzz.fizzbuzz(1),1)
        self.assertEqual(fizzbuzz.fizzbuzz(2),2)
    def testFizzBuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15),"fizzbuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(30),"fizzbuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(45),"fizzbuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(60),"fizzbuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(16),16)
        self.assertEqual(fizzbuzz.fizzbuzz(4),4)
        self.assertEqual(fizzbuzz.fizzbuzz(1),1)
        self.assertEqual(fizzbuzz.fizzbuzz(2),2)

if __name__ == '__main__':
    unittest.main()