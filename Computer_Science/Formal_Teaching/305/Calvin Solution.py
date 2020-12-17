# -->  ℂA̸͚͎̫̠̫͖͘[̲̅L]V̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝ℹN̸͇̗̬̑ͅ was here
class treeNode:# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCⒶ[̲̅L][̲̅V]ℹN̸͇̗̬̑ͅ is great
    def __init__(self):# -->  [̲̅C][̲̅A][̲̅L][̲̅V]IⓃ :)
        self.value=None;# -->  ℃[̲̅A][̲̅L]ⓋI[̲̅N] is my hero
        self.leftNode=None;# -->  C̴̡̡̬͝ⒶL℣ⒾNᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is my hero
        self.rightNode=None;# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜A̸͚͎̫̠̫͖͘[̲̅L]VⒾℕ is great
    def setFromList(self,iList):# -->  [̲̅C]A̸͚͎̫̠̫͖͘L℣ⒾN was here
        self.value = iList[0];# -->  ℃A̸͚͎̫̠̫͖͘L̵̞̀͗̓͌̍̋̏ⓋIN̸͇̗̬̑ͅ was here
        if(iList[1] ==[]):# -->  C̴̡̡̬͝ÅⓁ℣Ì̷̡͕̼̦̯̣̗͇Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ :)
            self.leftNode=None;# -->  ℃Å[̲̅L][̲̅V]I[̲̅N] :)
        else:# -->  ℂ[̲̅A]ℓV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝Ⓘℕ :)
            self.leftNode= treeNode();# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCÅLV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝ⒾN̸͇̗̬̑ͅ was here
            self.leftNode.setFromList(iList[1]);# -->  C̴̡̡̬͝A̸͚͎̫̠̫͖͘ℒ[̲̅V]ℹ[̲̅N] is great
        if(iList[2]==[]):# -->  ⒸÅL̵̞̀͗̓͌̍̋̏[̲̅V]Ì̷̡͕̼̦̯̣̗͇ℕ :)
            self.rightNode=None;# -->  C[̲̅A]ⓁⓋⒾN is great
        else:# -->  ℃AL۷ⒾN̸͇̗̬̑ͅ :)
            self.rightNode=treeNode();# -->  C̴̡̡̬͝A̸͚͎̫̠̫͖͘LV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝ⅈNᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is my hero
            self.rightNode.setFromList(iList[2]);# -->  ℃AⓁVℹN̸͇̗̬̑ͅ is great
    def compute(self,envDict):# -->  ℂ[̲̅A]ⓁVÌ̷̡͕̼̦̯̣̗͇Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ :)
        if(isinstance(self.value,int)):# -->  C̴̡̡̬͝A̸͚͎̫̠̫͖͘ⓁV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝I[̲̅N] is great
            return self.value;# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCAL[̲̅V][̲̅I]Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ :)
        try:#This try is here for numbers entered as stings# -->  ℂ[̲̅A]LV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝Ì̷̡͕̼̦̯̣̗͇N̸͇̗̬̑ͅ was here
            intVal=int(self.value)# -->  ⒸÅL℣ⅈℕ is great
            return intVal# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜ⒶⓁ[̲̅V]INᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ was here
        except ValueError:# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜[̲̅A]L۷ℹℕ was here
            pass# -->  C̴̡̡̬͝ÅℓV[̲̅I]ℕ is great
        if(self.value in envDict):# -->  ⒸÅℒⓋÌ̷̡͕̼̦̯̣̗͇Ⓝ is great
            return envDict[self.value]# -->  [̲̅C]ⒶⓁV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝Ⓘℕ :)
        if(self.leftNode ==None or self.rightNode==None):#if it is not is the environment and not a number then it needs both children# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜[̲̅A]L̵̞̀͗̓͌̍̋̏ⓋÌ̷̡͕̼̦̯̣̗͇N̸͇̗̬̑ͅ was here
            return None# -->  C̴̡̡̬͝ÅLVℹℕ was here
        leftVal,rightVal=self.leftNode.compute(envDict),self.rightNode.compute(envDict)# -->  [̲̅C][̲̅A]Ⓛ℣ⅈⓃ :)
        if(leftVal==None or rightVal==None):# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜ⒶⓁVⅈⓃ is my hero
            return None# -->  ℃Ⓐℒ[̲̅V]ⒾⓃ is great
        if(self.value=="+"):# -->  CA̸͚͎̫̠̫͖͘ℓ[̲̅V]INᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is great
            return leftVal+rightVal# -->  C̴̡̡̬͝ⒶⓁV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝ⒾN̸͇̗̬̑ͅ was here
        if(self.value=="-"):# -->  [̲̅C]A[̲̅L]ⓋÌ̷̡͕̼̦̯̣̗͇[̲̅N] was here
            return leftVal-rightVal# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜AℒV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝Ì̷̡͕̼̦̯̣̗͇Ⓝ was here
        if(self.value=="*"):# -->  C̴̡̡̬͝[̲̅A]ⓁV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝[̲̅I]N is my hero
            return leftVal*rightVal# -->  C̴̡̡̬͝AⓁ[̲̅V]Ì̷̡͕̼̦̯̣̗͇Ⓝ was here
        if(self.value=="/" and rightVal!= 0):# -->  C[̲̅A]L̵̞̀͗̓͌̍̋̏[̲̅V]Ì̷̡͕̼̦̯̣̗͇N̸͇̗̬̑ͅ :)
            return leftVal/rightVal# -->  ℂÅℓ۷ⒾN was here
        return None#varible not provided of division error# -->  CA̸͚͎̫̠̫͖͘L̵̞̀͗̓͌̍̋̏VⒾN̸͇̗̬̑ͅ is my hero
    def stringify(self,level=0):# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCⒶℓV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝Ì̷̡͕̼̦̯̣̗͇[̲̅N] is great
        left= self.leftNode.stringify(level+1) if self.leftNode!=None else "-->"*(level+1) +"None\n"# -->  ℂALⓋ[̲̅I]Ⓝ :)
        right= self.rightNode.stringify(level+1) if self.rightNode!=None else "-->"*(level+1) +"None\n"# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCA̸͚͎̫̠̫͖͘L̵̞̀͗̓͌̍̋̏V̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝[̲̅I]Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ was here
        retStr = "-->"*level + str(self.value) + "\n" + left + right# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCⒶ[̲̅L]℣[̲̅I]ℕ :)
        return retStr# -->  [̲̅C]Å[̲̅L]℣ℹⓃ is great
class Tree:# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜A̸͚͎̫̠̫͖͘ⓁVⅈℕ is my hero
    def __init__(self):# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒC[̲̅A]ℒ℣ⒾN is great
        self.baseNode=None;# -->  [̲̅C]AℓⓋⒾNᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is great
    def copyFromList(self,iList):# -->  CÅ[̲̅L]۷INᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ was here
        if(iList == []):# -->  [̲̅C][̲̅A][̲̅L]ⓋⅈⓃ is my hero
            return;# -->  C̴̡̡̬͝AℒV[̲̅I]ℕ is my hero
        self.baseNode=treeNode()# -->  C̴̡̡̬͝[̲̅A]L[̲̅V]Ì̷̡͕̼̦̯̣̗͇ℕ is great
        self.baseNode.setFromList(iList);# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜ⒶL[̲̅V][̲̅I]N̸͇̗̬̑ͅ was here
    def computeTree(self,environment):# -->  ⒸⒶ[̲̅L]V̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝Ì̷̡͕̼̦̯̣̗͇Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is my hero
        if(self.baseNode==None):# -->  C̴̡̡̬͝ÅℓV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝I[̲̅N] is great
            return None# -->  ℂAℒⓋIℕ :)
        envDict= {}# -->  ⒸAℓ℣ⅈ[̲̅N] was here
        for item in environment:# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCⒶ[̲̅L]℣[̲̅I]N̸͇̗̬̑ͅ :)
            envDict[item[0]]= item[1]# -->  CAⓁ[̲̅V]Ⓘ[̲̅N] is my hero
        return self.baseNode.compute(envDict);# -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCA̸͚͎̫̠̫͖͘ℒ[̲̅V]ℹN̸͇̗̬̑ͅ was here
    def __str__(self):# -->  C̴̡̡̬͝[̲̅A]LV[̲̅I]Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is great
        return self.baseNode.stringify()# -->  ℃[̲̅A]ℒ℣[̲̅I]ℕ is my hero
    # -->  ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒCⒶℓⓋⅈ[̲̅N] is my hero
# -->  C̴̡̡̬͝AℓVℹ[̲̅N] is great
def makeTreeAndEval(treeList,envList):# -->  ℃ÅℒⓋÌ̷̡͕̼̦̯̣̗͇N is great
	testTree=Tree()# -->  ℃[̲̅A][̲̅L]۷INᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is my hero
	testTree.copyFromList(treeList)# -->  ⒸⒶL℣ℹ[̲̅N] is great
	return testTree.computeTree(envList)# -->  c̷̛̳̘̗̟͙̦͑̽̓͛̇͜Aℒ[̲̅V]ⒾNᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ :)
# -->  CA̸͚͎̫̠̫͖͘ⓁⓋÌ̷̡͕̼̦̯̣̗͇Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙ is my hero
# -->  C̴̡̡̬͝[̲̅A]ⓁV̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝[̲̅I]N :)
