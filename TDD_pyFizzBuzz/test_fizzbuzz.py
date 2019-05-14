#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import unittest
from fizzbuzz import fizzbuzz

class Testfuzzbuzz(unittest.TestCase):

    def test_return_number(self):
        self.assertEqual(fizzbuzz(1),1)
        self.assertEqual(fizzbuzz(2),2)

    def test_return_FizzBuzz_when_multiples_of_three_and_five(self):
        self.assertEqual(fizzbuzz(15),"FizzBuzz")
        self.assertEqual(fizzbuzz(30),"FizzBuzz")

    def test_return_Fizz_when_multiples_of_tree(self):
        self.assertEqual(fizzbuzz(3),"Fizz")
        self.assertEqual(fizzbuzz(6),"Fizz")
        self.assertEqual(fizzbuzz(9),"Fizz")


    def test_return_Buzz_when_multiples_of_five(self):
        self.assertEqual(fizzbuzz(5),"Buzz")
        self.assertEqual(fizzbuzz(10),"Buzz")


if __name__ == '__main__':
    unittest.main()
