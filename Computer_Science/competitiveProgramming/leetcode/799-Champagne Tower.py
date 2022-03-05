# Runtime: 148 ms, faster than 65.05% of Python3 online submissions for Champagne Tower.
# Memory Usage: 14.1 MB, less than 67.48% of Python3 online submissions for Champagne Tower.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pass
        memo = [ [None]*100 for x in range(100)]
        memo[0][0] = max(0,poured - 1)
        if query_row == 0 and query_glass ==0:
            return min(1,poured)
        l = self.find_overflow(query_row-1,query_glass-1,memo)/2
        r = self.find_overflow(query_row-1,query_glass,memo)/2
        return min(1,l+r)


        
    def find_overflow(self,i,j,memo):
        if i <0 or j<0 or i>99 or j>99:
            return 0
        if not memo[i][j] is None:
            return memo[i][j]
        if j > i:#no glass here
            memo[i][j] = 0
            return 0
        overspill = (self.find_overflow(i-1,j-1,memo)+self.find_overflow(i-1,j,memo) )/2 
        overspill = max(0, overspill - 1) 
        memo[i][j] = overspill
        return overspill

    def __test_cases__(self):
        return [
            ({'poured':2,'query_row':1,'query_glass':1},0.5),
            ({'poured':0,'query_row':1,'query_glass':0},0)
        ]
    def __run__(self,**kwargs):
        return self.champagneTower(**kwargs)