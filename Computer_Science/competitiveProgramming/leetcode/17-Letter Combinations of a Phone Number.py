# Runtime: 185 ms, faster than 5.81% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 23.2 MB, less than 17.34% of Python3 online submissions for Letter Combinations of a Phone Number.

# Backtracking solution same results

class Solution:
    def letterCombinations(self, digits: str):
        ref = {
            '2':list('abc'),
            '3':list('def'),
            '4':list('ghi'),
            '5':list('jkl'),
            '6':list('mno'),
            '7':list('pqrs'),
            '8':list('tuv'),
            '9':list('wxyz'),
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return ref[digits[0]]
        builder = ref[digits[0]]
        for dig in digits[1:]:
            builder = self.combine(builder,ref[dig])
        return builder


    def combine(self, base,extension):
        res = []
        for b in base:
            for e in extension:
                res.append(b+e)
        return res
        
    def back_track(self,digits):
        ref = {
            '2':list('abc'),
            '3':list('def'),
            '4':list('ghi'),
            '5':list('jkl'),
            '6':list('mno'),
            '7':list('pqrs'),
            '8':list('tuv'),
            '9':list('wxyz'),
        }
        res = []
        def sub(current):
            if len(current) == len(digits):
                res.append(current)
                return 
            cur_dig = digits[len(current)]
            for char in ref[cur_dig]:
                sub(current + char)