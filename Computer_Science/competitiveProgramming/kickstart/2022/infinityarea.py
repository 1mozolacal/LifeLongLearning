import math

for test_case in range(int(input())):
    
    
    r,a,b = [int(x) for x in input().split(' ')]
    cur_r = r
    summation = 0
    is_right = True
    while cur_r > 0:
        summation += math.pi * cur_r * cur_r
        if is_right:
            cur_r = cur_r * a
        else:
            cur_r = cur_r // b
        is_right = not is_right
    print(f"Case #{test_case + 1}: {summation}")