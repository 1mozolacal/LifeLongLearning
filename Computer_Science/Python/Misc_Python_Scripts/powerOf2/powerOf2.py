import sys

#First argument: is the pattern at the end that you are serching for
endding = sys.argv[1]
lengthOffEnd = len( endding)

for x in range(1000):
    num = pow(2,x)
    if( str(num)[-lengthOffEnd:] == endding ):
        print ("x of :" +  str(x) + " -->" + str( pow(2, x)) )
    #else:
        #print( "not: " + str(num)[-lengthOffEnd:] )