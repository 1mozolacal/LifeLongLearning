
for test_case in range(int(input())):
    
    amount = int(input())
    values = [int(x) for x in input().split(' ')]
    
    l,r = 0,len(values)-1
    cur_max = 0
    counter = 0
    while l <= r:
        if values[l] < values[r]:
            if cur_max == 0 or values[l] >= cur_max:
                counter +=1
                cur_max = max(cur_max, values[l])
            l+=1
        else:
            if cur_max == 0 or values[r] >= cur_max:
                counter +=1
                cur_max = max(cur_max, values[r])
            r-=1
    print(f"Case #{test_case+1}: {counter}")
        
        