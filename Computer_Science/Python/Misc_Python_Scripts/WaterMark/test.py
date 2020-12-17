
class treeNode:
    def __init__(self):
        self.value=None;
        self.leftNode=None;
        self.rightNode=None;
    def setFromList(self,iList):
        self.value = iList[0];
        if(iList[1] ==[]):
            self.leftNode=None;
        else:
            self.leftNode= treeNode();
            self.leftNode.setFromList(iList[1]);
        if(iList[2]==[]):
            self.rightNode=None;
        else:
            self.rightNode=treeNode();
            self.rightNode.setFromList(iList[2]);
    def compute(self,envDict):
        if(isinstance(self.value,int)):
            return self.value;
        try:#This try is here for numbers entered as stings
            intVal=int(self.value)
            return intVal
        except ValueError:
            pass
        if(self.value in envDict):
            return envDict[self.value]
        if(self.leftNode ==None or self.rightNode==None):#if it is not is the environment and not a number then it needs both children
            return None
        leftVal,rightVal=self.leftNode.compute(envDict),self.rightNode.compute(envDict)
        if(leftVal==None or rightVal==None):
            return None
        if(self.value=="+"):
            return leftVal+rightVal
        if(self.value=="-"):
            return leftVal-rightVal
        if(self.value=="*"):
            return leftVal*rightVal
        if(self.value=="/" and rightVal!= 0):
            return leftVal/rightVal
        return None#varible not provided of division error
    def stringify(self,level=0):
        left= self.leftNode.stringify(level+1) if self.leftNode!=None else "-->"*(level+1) +"None\n"
        right= self.rightNode.stringify(level+1) if self.rightNode!=None else "-->"*(level+1) +"None\n"
        retStr = "-->"*level + str(self.value) + "\n" + left + right
        return retStr
class Tree:
    def __init__(self):
        self.baseNode=None;
    def copyFromList(self,iList):
        if(iList == []):
            return;
        self.baseNode=treeNode()
        self.baseNode.setFromList(iList);
    def computeTree(self,environment):
        if(self.baseNode==None):
            return None
        envDict= {}
        for item in environment:
            envDict[item[0]]= item[1]
        return self.baseNode.compute(envDict);
    def __str__(self):
        return self.baseNode.stringify()
    

def makeTreeAndEval(treeList,envList):
	testTree=Tree()
	testTree.copyFromList(treeList)
	return testTree.computeTree(envList)


