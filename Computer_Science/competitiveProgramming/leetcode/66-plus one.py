class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int(''.join([str(x) for x in digits]))
        x += 1
        ret = []
        for letter in str(x):
            ret.append(int(letter))
        return ret
            