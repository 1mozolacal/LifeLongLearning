import unittest
import mySolution

#self.assertEqual( first, answe, message)

class tester(unittest.TestCase):

    def runArrayTest(self, array,function):
        for test in array:
            functionAnswer = function( test[0])
            message = "\nFailed at {input}\nExpecting {output}\nRecieved {fun}".format(input=test[0],output=test[1],fun=functionAnswer)
            self.assertEqual(functionAnswer, test[1], message )

    def test_infixToPostfix(self):
        testCases = [
        ['( 2 + 2 ) ! + 8', '2 2 + ! 8 +']
        ]
        self.runArrayTest(testCases, self.returnInfixToPostfixAsString)

    def returnInfixToPostfixAsString(self,input):
        list = mySolution.infixToPostfix(input)
        return " ".join(list.getListRef())

    def test_postfixEval(self):
        testCases = [
        ['2 2 + ! 8 +'.split(' '), 32]
        ]
        self.runArrayTest(testCases, mySolution.postfixEval)

    def test_Factorial(self):
        testCases = [
        [0,1],
        [1,1],
        [2,2],
        [3,6],
        [4,24],
        [5,120],
        [6,720],
        [7,5040],
        [8,40320],
        [9,362880],
        [10,3628800],
        [20,2432902008176640000],
        ]

        self.runArrayTest(testCases,mySolution.factorial)

    def test_infixToPostfixEval(self):
        testCases = [
        ['( 2 + 2 ) ! + 8', ['2 2 + ! 8 +'.split(' '),32] ]
        ]
        self.runArrayTest(testCases,mySolution.infixToPostfixEval)

    def test_infixToPostfixException(self):
        with self.assertRaises(ValueError) as context:#makes sure a valueError excepttion is raised
            mySolution.infixToPostfix('( 2 + 2 ) ) ! + 8')
        with self.assertRaises(ValueError) as context:#makes sure a valueError excepttion is raised
            mySolution.infixToPostfix('( ( 2 + 2 ) ! + 8')



if __name__ == '__main__':
    unittest.main()
