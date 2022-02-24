# Runtime: 42 ms, faster than 49.67% of Python3 online submissions for Rectangle Overlap.
# Memory Usage: 13.9 MB, less than 65.90% of Python3 online submissions for Rectangle Overlap.

#Second solution
# Runtime: 42 ms, faster than 49.67% of Python3 online submissions for Rectangle Overlap.
# Memory Usage: 14 MB, less than 55.17% of Python3 online submissions for Rectangle Overlap.

class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        min_x_1,min_y_1,max_x_1,max_y_1 = rec1
        min_x_2,min_y_2,max_x_2,max_y_2 = rec2
        x_intercepts = self.sub(min_x_1,max_x_1,min_x_2,max_x_2)
        y_intercepts = self.sub(min_y_1,max_y_1,min_y_2,max_y_2)
        return x_intercepts and y_intercepts
    def sub(self, min_1,max_1,min_2,max_2) -> bool:
        a = (min_1 < min_2 < max_1) or (min_1 < max_2 < max_1)
        b = (min_2 < min_1 < max_2) or (min_2 < max_1 < max_2)
        return a or b
    
    def isRectangleOverlap_second_soltuion(self, rec1, rec2) -> bool:
        min_x_1,min_y_1,max_x_1,max_y_1 = rec1
        min_x_2,min_y_2,max_x_2,max_y_2 = rec2
        
        if max_x_1 <= min_x_2 or max_x_2 <= min_x_1:
            return False
        if max_y_1 <= min_y_2 or max_y_2 <= min_y_1:
            return False
        
        return True

    def __test_cases__(self):
        return [
            ({"rec1":[0,0,2,2],"rec2":[1,1,3,3]},'true')
        ]
    def __run__(self, **kwargs):
        return self.isRectangleOverlap(**kwargs)