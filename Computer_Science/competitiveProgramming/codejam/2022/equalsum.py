
def hit_target(target,index,nums,working_set,s_ws):

    if index < 0:
        return False
    
    s = s_ws
    for i in range(index,-1,-1):
        if nums[i] + s == target:
            return [nums[i]]
        elif nums[i] + s < target:
            ws = working_set[:]
            ws.append(nums[i])
            ret = hit_target(target,i-1,nums,ws,sum(ws))
            if ret:
                ret.append(nums[i])
                return ret
    
    return False
    


for case_num in range(int(input())):

    n = int(input())

    #pick n numbers
    my_nums = [x+1 for x in range(n)]
    print(' '.join([str(x) for x in my_nums]))

    other_num = [int(x) for x in input().split(' ')]
    
    my_nums.extend(other_num)
    s = sum(my_nums)
    my_nums.sort()

    my_set = hit_target(s/2,len(my_nums)-1,my_nums,[],0)

    print(' '.join([str(x) for x in my_set]))



    
