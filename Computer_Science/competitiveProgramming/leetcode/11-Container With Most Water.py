


class Solution:
    def maxArea(self,heights):
        left_selection = 0
        left_pointer = 0
        rigth_selection = len(heights)-1
        right_pointer = len(heights)-1

        current_max = min(heights[0],heights[rigth_selection]) * rigth_selection

        while True:
            left_pointer = None
            right_pointer = None
            for i,val in enumerate(heights[left_selection:]):
                if val > heights[left_selection]:
                    left_pointer = i
                    break
            for i,val in enumerate(heights[:rigth_selection]):
                if val > heights[rigth_selection]:
                    right_pointer = i
                    break
            
            if left_pointer is None or right_pointer is None or left_pointer > right_pointer:
                break

            situations = [ (left_pointer,right_pointer),(left_pointer,rigth_selection),(left_selection,right_pointer) ]
            sit_sort = sorted(situations, reverse=True,key= lambda x: min(heights[x[0]],heights[x[1]]) * abs(x[0]-x[1]) )
            t =sit_sort[0]
            if min(t[0],t[1]) * abs(t[0]-t[1]) > current_max:
                break
            left_selection,rigth_selection = t

        return current_max



#Time limit exceeded
'''
class Solution:
    def maxArea(self, heights) -> int:
        volume = 0
        for index,height in enumerate(heights):
            values = [ min(height,h)*abs(index-i) for i,h in enumerate(heights) if i != index]
            values.append(volume)
            volume = max(values)
        return volume
'''