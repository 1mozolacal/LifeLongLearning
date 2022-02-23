# Runtime: 59 ms, faster than 7.35% of Python3 online submissions for Nth Digit.
# Memory Usage: 13.9 MB, less than 68.60% of Python3 online submissions for Nth Digit.

class Solution:


    def findNthDigit(self, n: int) -> int:
        
        in_layer = 0
        start_of_layer = 0
        counter = 0
        for layer in range(1,100):
            counter += self.amount_in_layer(layer)
            if counter >= n:
                in_layer = layer
                break
            else:
                start_of_layer += self.amount_in_layer(layer)
        
        jump_in_layer = int((n-start_of_layer-1)/in_layer)
        index = (n-start_of_layer-1) % in_layer
        string_int = str( 10 ** (in_layer-1) + jump_in_layer )
        
        return string_int[index]
            
        
    def amount_in_layer(self,layer_num):
        amount = self.amount_in_layer_sub(layer_num)
        if layer_num == 1:
            return amount - 1
        return amount
    
    def amount_in_layer_sub(self,layer_num):
        total = 10 ** layer_num
        if(layer_num == 1):
            return total
        return (total - (10 ** (layer_num - 1)) ) * layer_num

    
    def __test_cases__(self):
        return [
            ({"n":10000},'7')
        ]
    def __run__(self, **kwargs):
        return self.findNthDigit(**kwargs)
        