# Runtime: 29 ms, faster than 97.04% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 74.41% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = nums1[:m]
        n2 = nums2[:n]
        n1.extend(n2)
        n1.sort()
        nums1[:] = n1[:]