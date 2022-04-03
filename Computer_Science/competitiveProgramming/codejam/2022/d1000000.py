
for test in range(int(input())):
    dice = int(input())
    die = [int(x) for x in input().split(' ')]
    
    die.sort()
    counter = 0
    for i,d in enumerate(die):
        if d > counter:
            counter+=1
    print(f'Case #{test+1}: {counter}')