import unittest # for building test cases
from RSI_Interview_question import answerClass

# class to hold aboveBelow method test cases
class aboveBelowTesting(unittest.TestCase):

    def setUp(self):
        pass

    def test_example(self):
        rsp = answerClass.aboveBelow([1,5,2,1,10], 6)
        self.assertEqual(rsp, {'above':1, 'below':4})

    def test_negNumbers(self):
        rsp = answerClass.aboveBelow([-50,-20,0,57,-102,4], 13)
        self.assertEqual(rsp, {'above':1, 'below':5})

    def test_noInput(self):
        with self.assertRaises(Exception):
            answerClass.aboveBelow()
            answerClass.aboveBelow([],)

# class to hold stringRotaiton test cases.
class stringRotationTesting(unittest.TestCase):
    def test_example(self):
        rsp = answerClass.stringRotation('MyString', 2)
        self.assertEqual(rsp, 'ngMyStri')

    def test_rotateThroughAll(self):
        for i in range(20):
            rsp = answerClass.stringRotation('MyString', i)
            self.assertEqual(rsp, 'MyString'[-i%8:]+'MyString'[:-i%8])

    def test_noInput(self):
        rsp = answerClass.stringRotation('', 3)
        self.assertEqual(rsp, '')
        rsp = answerClass.stringRotation('MyString', 0)
        self.assertEqual(rsp, 'MyString')
        with self.assertRaises(Exception):
            answerClass.stringRotaiton()
            answerClass.stringRotaiton('MyString')

if __name__ == '__main__':
    unittest.main()
