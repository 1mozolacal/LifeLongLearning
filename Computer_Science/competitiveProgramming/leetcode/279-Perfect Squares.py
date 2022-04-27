import math

class Solution:
    def numSquares(self, n: int) -> int:
        
        counter = 0
        cur_square = math.floor(math.sqrt(n))
        working_n = n
        while working_n > 0:
            if cur_square**2 <= working_n:
                working_n -= cur_square**2
                counter+=1
            else:
                cur_square = math.floor(math.sqrt(working_n))
        return counter