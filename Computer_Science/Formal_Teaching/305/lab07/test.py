import unittest
import eval

class testTreeEval(unittest.TestCase):
    def runTestCases(self,testCases, function):#runs throught all the test cases
        for test in testCases:
            functionAnswer = function( *test[0] )
            printString = "With {argu} got {answer} expected {correct}".format(argu=test[0],answer=functionAnswer,correct=test[1])
            self.assertEqual(functionAnswer,test[1],printString)#TODO

    def testTreeEval(self):
        testCases=[
            [ [ ["10",[],[]] , [["a",10],["b",20],["c",40] ] ],10 ],
            [ [ ["+", ["a", [], []], ["*", ["b", [], []], ["c", [], []]]] ,[["a", 10], ["b", 20],["c",30]] ] ,610 ],
            [[["+", ["a", [], []], ["*", ["b", [], []], ["c", [], []]]], [["a", 10], ["b", 20]]], None],
            [[["+", ["a", [], []], ["100", ["b", [], []], ["c", [], []]]], [["a", 10], ["b", 20], ["c", 30]]], 110],
            [[ ["/",["a",[],[]],["0",[],[]]] , [["a", 10], ["b", 20], ["random", 30]]], None],
            [ [ [] , []] , None],
            [ [  ["+",["*",["/",["+",["Calvin",[],[]],["*",["-",["Double",[],[]],["Double",[],[]]],["0",[],[]]]],["Blue",[],[]]],[3,[],[]]],["-5",[],[]] ] ,[["Double",2],["Calvin",10],["Blue",5]]  ] , 1 ]
        ]
        self.runTestCases(testCases,eval.makeTreeAndEval)


if __name__ == '__main__':
    unittest.main()
