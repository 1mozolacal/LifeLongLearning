
'''
This is the most straight forwards solution
'''
# class Solution:
#     def getStrongest(self, arr: List[int], k: int) -> List[int]:
#         arr.sort()
#         m = arr[math.floor((len(arr)-1)/2)]
#         def key_val(x):
#             val = abs(x-m)
#             if(x>m):
#                 return val*2 +1
#             else:
#                 return val*2
#         arr.sort(key= key_val )
#         arr.reverse()
#         return arr[:k]
