#this is a wrapper that will run your python solution class

my_import = __import__('400-Nth Digit')

my_solution = my_import.Solution()
test_cases = my_solution.__test_cases__()
for input,answer in test_cases:
    result = my_solution.__run__(**input)
    if result == answer:
        print("correct!")
    else:
        print(f"Expected {answer}. Got {result}. With input {input}")