import csv

file = open("copyPaste.txt","r")
lines = file.readlines()
formatedLines = []
for line in lines:
    parts = line.split(" ")
    lineToWrite = [parts[0],parts[1],parts[3][0:-1],parts[4],parts[5][0],parts[5][-1],parts[6],parts[7][0:-1],parts[8].strip()]
    formatedLines.append(lineToWrite)

with open('employee_file.csv', mode='w', newline='') as employee_file:
    csvWriter = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def findLine(lookingFor, current=0):
        if(current>0):
            lookUp = findLine(lookingFor, current*-1)
            if( lookUp != -1):
                return lookUp
        elif(current<0):
            if(int(formatedLines[(current*-1)-1][0]) ==lookingFor):
                return (current*-1)-1
            else:
                return -1
        for x in range( len(formatedLines) ):
            if(int(formatedLines[x][0]) ==lookingFor ):
                return x
        return None

    counter = 1;
    lastFound = 0;
    while True:
        found = findLine(counter,lastFound)
        #print("found " + str(counter) + " at " + str(found) )
        if(found == None):
            break;
        lastFound = found
        csvWriter.writerow( formatedLines[found] )
        counter+=1

print("donee")
