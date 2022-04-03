
MAX = 1000000
for test in range(int(input())):
    printers = []
    for printer in range(3):
        temp = input().split(' ')
        temp = [int(x) for x in temp]
        printers.append(temp)
    
    current_paint = 0
    colour = []
    for col in range(4):
        this_col = [x[col] for x in printers]
        select_col = min(this_col)
        sec_sel = min(select_col,MAX-current_paint)
        colour.append(sec_sel)
        current_paint+=sec_sel
    
    solution = 'IMPOSSIBLE' if sum(colour)<MAX else ' '.join([str(x) for x in colour])
    print(f'Case #{test+1}: {solution}')
    