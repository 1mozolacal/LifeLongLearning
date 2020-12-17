'''
By:Calvin Mozola
Data: April 21, 2020

Assumptions:
    Each student has written a test, if not, no info about them is displayed
    All test weights add to 100, if not, everyone get zero in that course
'''

import csv
import sys
import json


class StudentInfo():
    '''
    This class is for holding a students info and then generating the proper json output based on the info

    Attributes:
        id (String): used for knowing which student to give a mark to. Is used as an integer for final output
        name (String): will add this where needed for the final output
        courseInfo (list): contain a list of all courses. A course is a list that contains...
                                                                                        course id
                                                                                        list of all marks receieved by that student in that course
    '''

    def __init__(self,id,name):
        ''' Constructor that intialized id and name from parameters and courseInfo to empty list'''
        self.id = id
        self.name = name
        self.courseInfo = [] #list of [ (id of course), (list of all test taken)]
    
    def isYou(self,idToCheck):
        ''' Used to check if this students id matches give id'''
        return self.id==idToCheck
    
    #note:rawTestInfo isn't modified here
    def addMark(self, testId, mark, rawTestInfo):
        '''
        Adds a mark to a student
        
        First looks for what course it belongs to (if course doesn't exisit yet then it is made)
        Then add this mark to the list of marks in the proper course
        '''
        addedMark = False#flag if a new course need to made made for this test
        courseId = rawTestInfo[testId][0]
        for course in self.courseInfo:
            if(course[0] == courseId):
                addedMark = True
                course[1].append( [testId,mark] )
        if not addedMark:
            newCourse = [courseId, [[testId,mark]] ]
            self.courseInfo.append(newCourse)

    def getOutput(self, rawCourses, rawTests):
        ''' returns a dictionary with all the proper field for the json file  '''
        courseSum = 0#used in calc final average
        courseNumber = 0#used in calc for final average

        #go through list of courses and create proper json formatting
        courseOutput = []
        for course in self.courseInfo:
            courseAverage = self.getAverageOfCourse(course[1], rawTests)
            courseSum+= courseAverage
            courseNumber+=1

            courseOutput.append({
                "id":int(course[0]),
                "name":rawCourses[ course[0] ][0],
                "teacher":rawCourses[ course[0] ][1],
                "courseAverage": round(courseAverage,2)
            })

        output = {
            'id' : int(self.id),
            'name' : self.name,
            'totalAverage' : round( (courseSum/max(1,courseNumber)) ,2),#couseNumber should always be larger than 0 because a course is never added without a mark but the max(1,..) is to prevent zero divion
            'courses' : courseOutput
        }
        return output
        
    #courseTests is an list of all test in the form of [testId, mark achieved]
    def getAverageOfCourse(self, courseTests, rawTests):
        '''
        With a give list of marks from a course will return the course average.
        Note: if the course tests do not add up to 100(wrong input from csv files) then it will record mark as zero even if all test were completed
        '''
        coursePercentageCompete = 0
        runningAverage = 0
        for test in courseTests:
            weigth = int(rawTests[ test[0] ][1] )
            runningAverage += (test[1]/100.0) * weigth #test[1] is the mark of the test
            coursePercentageCompete += weigth
        if coursePercentageCompete == 100:
            return runningAverage#for round to tow decimal places
        return 0#they didn't complete all tests

    def __lt__(self,otherStudent):
        ''' compare between StudentInfos for sorting. Allows the use of built in sort methods'''
        return self.id < otherStudent.id



def main():
    '''
    The main entery point for this script.
    '''
    systemArgs = sys.argv
    numberOfArgs = len(systemArgs) - 1 #subtract one for the name of the program
    if(numberOfArgs !=5):
        print("Invalid number of parameter passed")
        exit(1)
    
    #get system varibles form command line
    pathToCourses = systemArgs[1]
    pathToStudents =systemArgs[2]
    pathToTests =systemArgs[3]
    pathToMarks =systemArgs[4]
    pathToOutput = systemArgs[5]
    
    #parse the csv files
    rawCourses = parseFileToDict(pathToCourses)
    rawStudents = parseFileToDict(pathToStudents)
    rawTests = parseFileToDict(pathToTests)
    #parse the marks(what is returen is order list of StudentInfo)
    studentInfo = parseMarks(pathToMarks, rawStudents, rawTests)
    
    #create final output
    finalOutput = {}
    finalOutput['students'] =[]
    for student in studentInfo:
        finalOutput['students'].append( student.getOutput(rawCourses, rawTests) )

    with open(pathToOutput,'w') as outputFile:
        json.dump(finalOutput, outputFile)#to in json formate to file
      


def parseFileToDict(filePath):
    '''
    parse the info from the csv file. Leaves all values as strings and return as a dict with the ids as keys.
    works the tests, students, and coursese not the marks
    '''
    with open(filePath) as readingFile:
        allLines = csv.reader(readingFile,delimiter=',')
        skipFirstLine = True#skips titles
        returnDict = {}
        for line in allLines:
            if skipFirstLine or (line==[]):#for skiping first line and empty lines
                skipFirstLine=False
                continue
            returnDict[line[0]] = line[1:]
    return returnDict

def parseMarks(filePath, dictOfRawStudents, dictOfRawTests):
    '''
    Parses throught marks file and builds a list of StudentInfo added each test to the appropriate student
    '''
    with open(filePath) as readingFile:
        allLines = csv.reader(readingFile,delimiter=',')
        skipFirstLine = True#skips titles
        students = []#list of StudentInfo
        for line in allLines:
            if skipFirstLine or (line==[]):#for skiping first line and empty lines
                skipFirstLine = False
                continue
            
            #parse mark info
            currentTest = line[0]
            currentStudentId = line[1]
            mark = int(line[2])

            #addes mark to appropriate student
            foundStudent = False
            for student in students:
                if( student.isYou(currentStudentId) ):
                    foundStudent=True
                    student.addMark(currentTest,mark,dictOfRawTests)
                    break
            if not foundStudent:#if that student doesn't current exist, create it
                newStudent =  StudentInfo(currentStudentId,dictOfRawStudents[currentStudentId][0])
                newStudent.addMark(currentTest,mark,dictOfRawTests)
                students.append( newStudent )
    
    students.sort()
    return students
                
#ensures that this file is the target of execution
if __name__ == "__main__":
    main()