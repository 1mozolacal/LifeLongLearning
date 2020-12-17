#This was quick a dirt to save time of manually making insert query by cleaning the generated data off https://www.generatedata.com/
# no error checking assumes perfect formatting
#Can only have one VALUES
#only parse off first line

#import os
#print(os.getcwd())

###Things that need to be changed
rawFile =  open('helperParser/raw.txt')
outputFile = "out.txt"
dataFormat = ["num","num","num","latlon","num","num","str","str","str","str"] #supports date, num, and latlon everything eles is null(plain string)
###End of thing that need to be changed

def parseString(input):
    return "'"+input+"'"
def dateParse(input):
    return "TO_TIMESTAMP('" + input + " 14:00:00', 'YYYY-MM-DD HH24:MI:SS')"

def numParse(input):
    return input

def latlonParse(input):
    return input

rawString = rawFile.readline()

header = rawString.split("VALUES")[0]
body = rawString.split("VALUES")[1]


stack = []
valuesList = []

currentValue = []
currentStr = ""
finishReadingStr = False
currentNonStr = ""
for char in body:
    if len(stack) == 0:
        if char == "(":
            stack.append("(")
        continue
    
    if stack[-1] == '"':
        if char == '"':
            stack.pop()
            finishReadingStr=True
        else:
            currentStr+=char

    elif stack[-1] == "(":
        if char == ",":
            if finishReadingStr:
                currentValue.append(currentStr)
                finishReadingStr=False
            else:
                currentValue.append(currentNonStr)
            currentNonStr=''
            currentStr=''
        elif char == '"':
            stack.append('"')
            currentNonStr=''
            currentStr=''
        elif char == ")":
            if finishReadingStr:
                currentValue.append(currentStr)
                finishReadingStr=False
            else:
                currentValue.append(currentNonStr)
            valuesList.append(currentValue)
            currentValue=[]
            currentNonStr=''
            currentStr=''
            stack.pop()
        else:
            currentNonStr+=char
    ###
    

writer = open(outputFile,'w')

firstLine = header + " VALUES\n"
writer.write(firstLine)

for val in valuesList:
    line = "("
    for index,element in enumerate(val):
        if index>0:
            line+=','
        
        if(dataFormat[index] is None or dataFormat[index] == "str"):#note - note checking
            line+=parseString(element)
        elif(dataFormat[index] == "num"):
            line+=numParse(element)
        elif(dataFormat[index] == "date"):
            line+=dateParse(element)
        elif(dataFormat[index] == "latlon"):
            line+=latlonParse(element)
    line+="),\n"
    writer.write(line)


