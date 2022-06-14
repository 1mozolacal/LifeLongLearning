


for case_num in range(int(input())):
    word = input()
    end_word = ''
    maybe_stack = ''
    
    for i in range(1,len(word)):
        cur = word[i-1]
        next = word[i]
        
        if cur < next:
            if maybe_stack != '':
                maybe_stack += cur
                end_word += maybe_stack * 2
                maybe_stack = ''
            else:
                end_word += cur *2 
        elif cur > next:
            end_word += maybe_stack
            maybe_stack = ''
            end_word += cur
        else:
            maybe_stack += cur
            
    if maybe_stack != '':
        maybe_stack += word[-1]
        end_word += maybe_stack
    else:
        end_word+= word[-1]
    
    print(f"Case #{case_num+1}: {end_word}")
        
    