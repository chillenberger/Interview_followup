# simple tests to veify answerClass is working correctly. 

import unittest # for building test cases
from RSI_Interview_Answer import answerClass

# class to hold aboveBelow method test cases
class aboveBelowTesting(unittest.TestCase):

    def test_example(self):
        rsp = answerClass.aboveBelow([1,5,2,1,10], 6)
        self.assertEqual(rsp, {'above':1, 'below':4})

    def test_negNumbers(self):
        rsp = answerClass.aboveBelow([-50,-20,0,57,-102,4], 13)
        self.assertEqual(rsp, {'above':1, 'below':5})

    def test_badInput(self):
        with self.assertRaises(Exception):
            answerClass.aboveBelow()
            answerClass.aboveBelow([])
            answerClass.aboveBelow([1,2,3,4], 1.2)

# class to hold stringRotaiton test cases.
class stringRotationTesting(unittest.TestCase):
    def test_example(self):
        rsp = answerClass.stringRotation('MyString', 2)
        self.assertEqual(rsp, 'ngMyStri')

    def test_rotateThroughAll(self):
        for i in range(20):
            rsp = answerClass.stringRotation('MyString', i)
            self.assertEqual(rsp, 'MyString'[-i%8:]+'MyString'[:-i%8])

    def test_badInput(self):
        rsp = answerClass.stringRotation('', 3)
        self.assertEqual(rsp, '')
        rsp = answerClass.stringRotation('MyString', 0)
        self.assertEqual(rsp, 'MyString')
        with self.assertRaises(Exception):
            answerClass.stringRotation()
            answerClass.stringRotation('MyString')
            answerClass.stringRotation('MyString', -2)

if __name__ == '__main__':
    unittest.main()
