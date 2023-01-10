class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0

        for col in range(len(strs[0])):
            pointer = strs[0][col]
            for row in range(1, len(strs)):
                if strs[row][col] < pointer:
                    delete_count += 1
                    break
                pointer = strs[row][col]

        return delete_count
