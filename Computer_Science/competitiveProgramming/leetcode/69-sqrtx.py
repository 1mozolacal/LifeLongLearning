class Solution:
    def mySqrt(self, x: int) -> int:

        number = 1
        while(True):
            if(number * number > x):
                return number - 1
            else:
                number +=1