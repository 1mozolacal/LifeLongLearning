
def calvinGroup(array, acc=[]):
    if(array==[]):
        return acc
    if(acc==[]):
        acc.append([array[0]])
        return calvinGroup(array[1:],acc)
    if(acc[-1][0]== array[0]):
        acc[-1].append(array[0])
        return calvinGroup(array[1:],acc)
    acc.append([array[0]])
    return calvinGroup(array[1:],acc)

print(calvinGroup([10,10,10,31,31,40,60,60,80]))
print("done")