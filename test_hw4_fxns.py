import unittest
import hw4_fxns
from hw4_fxns import calcCubeVol
from hw4_fxns import calcListAvg
from hw4_fxns import genFullName

class TestCase(unittest.TestCase):

        #Tests for Question 1
        def test_q1test1(self):
            self.assertEqual(calcCubeVol(4),64)
        def test_q1test2(self):
            self.assertRaises(ValueError,calcCubeVol("forty"))
        def test_q1test3(self):
            self.assertRaises(ValueError,calcCubeVol(-5))

        #Tests for Question 2
        def test_q2test1(self):
            self.assertEqual(calcListAvg([3,3,1,4,5]),3.2)

        def test_q2test2(self):
            self.assertRaises(ZeroDivisionError,calcListAvg([]))
        def test_q3test3(self):
            self.assertRaises(ValueError,calcListAvg([1,2,"abc"]))

        #Tests for Question 3
        def test_q3test1(self):
            self.assertEqual(genFullName("Kaavya","Subramanian"), "Kaavya Subramanian")
        def test_q3test2(self):
            self.assertEqual(genFullName("Wonder87", "Woman"), "Wonder87 Woman")
        def test_q3test3(self):
            self.assertRaises(ValueError,genFullName(95, "testing"))


if __name__ == '__main__':
    unittest.main()
