
for x in range(int(input())):
    print(f'Case #{(x+1)}:')
    row,col = input().split(' ')
    row = int(row)
    col = int(col)
    card = []
    line_row = list('-'.join(['+'] * (col + 1)))
    dot_row = list('.'.join(['|'] * (col +1)))
    for r in range(row):
        card.append(line_row[:])
        card.append(dot_row[:])
    card.append(line_row[:])
    card[0][0] = '.'
    card[0][1] = '.'
    card[1][0] = '.'
    for out_row in card:
        print(''.join(out_row))