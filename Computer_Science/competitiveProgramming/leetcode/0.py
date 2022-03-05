#this is a wrapper that will run your python solution class

my_import = __import__('799-Champagne Tower')

my_solution = my_import.Solution()
test_cases = my_solution.__test_cases__()
for input,answer in test_cases:
    result = my_solution.__run__(**input)
    if result == answer:
        print("correct!")
    else:
        print(f"Expected {answer}. Got {result}. With input {input}")


# Example
# class Solution:
#     def NAME(self, n: int) -> int:
#         pass
    
#     def __test_cases__(self):
#         return [
#             ({"varible":"value"},'expected answer')
#         ]
#     def __run__(self, **kwargs):
#         return self.NAME(**kwargs)
        