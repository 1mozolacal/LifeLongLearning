import unittest
import mySolution

class recuritionTester(unittest.TestCase):

    def runArrayTest(self, array,function):
        for test in array:
            functionAnswer = function( *test[0])
            message = "\nFailed at {input}\nExpecting {output}\nRecieved {fun}".format(input=test[0],output=test[1],fun=functionAnswer)
            self.assertEqual(functionAnswer, test[1], message )


    def test_power(self):
        testCases = [
            [[2,3],8],
            [[2, 5], 32],
            [[5, 5], 3125],
            [[9, 2], 81],
            [[10, 3], 1000],
            [[6, 8], 1679616],
            [[23, 2], 529]
        ]
        self.runArrayTest(testCases,mySolution.power)

    def test_powerH(self):
        testCases = [
            [[2, 3], 8],
            [[2, 5], 32],
            [[5, 5], 3125],
            [[9, 2], 81],
            [[10, 3], 1000],
            [[6, 8], 1679616],
            [[23, 2], 529]
        ]
        self.runArrayTest(testCases, mySolution.powerH)

    def test_binCo(self):
        #[column,row],answer
        testCases = [
            [[0,0],1],
            [[2,3],3],
            [[5,5],1],
            [[2,5],10],
            [[2,6],15],
            [[3,6],20]
        ]
        self.runArrayTest(testCases, mySolution.binomialCo)


if __name__ == '__main__':
    unittest.main()