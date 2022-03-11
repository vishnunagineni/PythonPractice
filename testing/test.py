import unittest
from unittest import result
from mysum import sum
from fractions import Fraction
class TestSum(unittest.TestCase):

    def test_sum(self):
        data=[1,2,3]
        result=sum(data)
        self.assertEqual(result,6)
    
    def test_sum_fraction(self):
        data=[Fraction(1,2),Fraction(1,4),Fraction(3,2)]
        result=sum(data)
        self.assertEqual(result,2)
    
if __name__=="__main__":
    unittest.main()