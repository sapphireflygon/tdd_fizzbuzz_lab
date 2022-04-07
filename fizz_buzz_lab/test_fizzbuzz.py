import unittest
from src_fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.test_number_normal = fizzbuzz(13)
        self.test_number_fizz = fizzbuzz(9)
        self.test_number_buzz = fizzbuzz(5)
        self.test_number_fizzbuzz = fizzbuzz(15)
        self.test_zero = fizzbuzz(0)
        self.test_neg_num = fizzbuzz(-15)
    

    # @unittest.skip("Delete this line to run the test")
    def test_zero_fails(self):
        self.assertEqual("The game starts at 1 you fool!", self.test_zero)
    
    # @unittest.skip("Delete this line to run the test")
    def test_neg_numbers_fails(self):
        self.assertEqual("The game starts at 1 you fool!", self.test_neg_num)
    
    # @unittest.skip("Delete this line to run the test")
    def test_fizzbuzz_equals_15(self):
        self.assertEqual("fizzbuzz", self.test_number_fizzbuzz)

    # @unittest.skip("Delete this line to run the test")
    def test_normal_number(self):
        self.assertEqual("13", self.test_number_normal)

    # @unittest.skip("Delete this line to run the test")
    def test_fizz_equals_9(self):
        self.assertEqual("fizz", self.test_number_fizz)

    # @unittest.skip("Delete this line to run the test")
    def test_buzz_equals_5(self):
        self.assertEqual("buzz", self.test_number_buzz)



    

