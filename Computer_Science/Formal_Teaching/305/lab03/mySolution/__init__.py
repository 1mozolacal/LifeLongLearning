

class Stack:
    def __init__(self):
        self.items = []
    def pop(self):
        return self.items.pop()
    def peek(self):#this will give an error if list is empty
        return self.items[ len(self.items)-1 ]
    def push(self,item):
        self.items.append(item)
    def isEmpty(self):
        return self.items == []
    def getListRef(self):
        return self.items

def infixToPostfix(equationStr):
    priorityOnStack = {
    '(':4,
    '!':3,
    '*':2,
    '/':2,
    '+':1,
    '-':1}
    priorityOffStack = {
    '(':0,
    '!':3,
    '*':2,
    '/':2,
    '+':1,
    '-':1}
    operationStack = Stack()
    outputStack = Stack()
    inputList = equationStr.split(" ")

    for element in inputList:
        if element in "+-*/!()":
            if element==')':#this is a special case that will unpop untill the next '('
                if( not '(' in operationStack.items):#error detection of invalid brakets at this point( too many ')' )
                    raise ValueError("No '(' to accompany the ')'")
                while (not operationStack.isEmpty() and not operationStack.peek()=='('):
                    outputStack.push( operationStack.pop())#unpop until the next
                operationStack.pop()#this pops off the '('
            elif (operationStack.isEmpty() ) or (priorityOnStack.get(element) > priorityOffStack.get(operationStack.peek()) ):#if new operator has higher priority
                operationStack.push(element)
            else:
                while(not operationStack.isEmpty() and priorityOnStack.get(element) <= priorityOffStack.get(operationStack.peek()) ):#unpop operationStack until you find a operatio with lower priority
                    outputStack.push( operationStack.pop())
                operationStack.push(element)
        else:
            outputStack.push(element)
    while(not operationStack.isEmpty()):
        if( operationStack.peek() == '('):#detection of invalid brakets (if there is left over '(' that where never closed)
            raise ValueError("Excess of '(' detected")
        outputStack.push( operationStack.pop())
    return outputStack

def postfixEval(equationList):
    elementHolder = Stack()

    #this lets operation have an arbitary number of operands
    numOfOperandPerOperation = {
    '!':1,
    '*':2,
    '/':2,
    '+':2,
    '-':2
    }

    for element in equationList:
        if(element in "+-*/!"):
            popOperands = []
            for x in range(numOfOperandPerOperation.get(element)):
                popOperands.append(elementHolder.pop())#could check for error here(not enoght items in the stack to pop)
            elementHolder.push(calc(element, popOperands))
        else:
            elementHolder.push(element)
        #could check for erro here (more than one thing left in the stack)
    return elementHolder.pop()


def calc(operation, operands):
    if operation == '!':
        return factorial(int(operands[0]))
    operands[0] = float(operands[0])
    operands[1] = float(operands[1])
    if operation == '+':
        return operands[0] + operands[1]
    elif operation == '-':
        return operands[0] - operands[1]
    elif operation == '*':
        return operands[0] * operands[1]
    elif operation == '/':
        return operands[0] / operands[1]


def factorial(num):
    counter = 1
    for x in range(2,num+1):
        counter *= x
    return counter

def infixToPostfixEval(inputStr):
    parts = infixToPostfix(inputStr).getListRef()#call getListRef because parts is a stack and it is needed as a list later on
    result = postfixEval(parts)
    #print("Input {input} \npost {po} \nresult {re}".format(input=inputStr,po=" ".join(map(str,parts)),re=result) )
    return [parts, result]


#print( infixToPostfix("( 2 + 2 ) ! + 8").getListRef() )
if( __name__ == '__main__' ):
    infixToPostfixEval("( 2 + 2 ) ! + 8")
