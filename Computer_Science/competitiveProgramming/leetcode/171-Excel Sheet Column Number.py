# Runtime: 55 ms, faster than 32.47% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.8 MB, less than 70.02% of Python3 online submissions for Excel Sheet Column Number.

# Second soltuion
# Runtime: 32 ms, faster than 92.31% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.9 MB, less than 70.02% of Python3 online submissions for Excel Sheet Column Number.

import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for letter in columnTitle:
            col_num *= len(string.ascii_uppercase)
            current_val = string.ascii_uppercase.index(letter) + 1
            col_num += current_val
        return col_num
    def titleToNumber_second_solution(self, columnTitle: str) -> int:
        col_num = 0
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for letter in columnTitle:
            col_num *= len(alpha)
            current_val = ord(letter) - 64
            col_num += current_val
        return col_num
print(string.ascii_uppercase)
