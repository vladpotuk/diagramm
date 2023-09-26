diagram_1 = int(input('Diagram 1  =  '))
diagram_2 = int(input('Diagram 2  =  '))
diagram_3 = int(input('Diagram 3  =  '))
target = int(input('Target = '))
size = 16

step_1 = size - int((size * ((diagram_1/target)*100))/100)
step_2 = size - int((size * ((diagram_2/target)*100))/100)
step_3 = size - int((size * ((diagram_3/target)*100))/100)
for i in range(0, size):
    for j in range(0, size):
        if 3 <= j <= 5 and i != size-1:
            if i >= step_1:
                print('*', end='')
            else:
                print(' ', end='')
        if 8 <= j <= 10 and i != size-1:
            if i >= step_2:
                print('@', end='')
            else:
                print(' ', end='')
        if 13 <= j <= 16 and i != size-1:
            if i >= step_3:
                print('$', end='')
            else:
                print(' ', end='')
        if j == 0:
            print('||', end='')
        elif i == size-1:
            print('==', end='')
        else:
            print(' ', end='')
    print()
print(f'\t{diagram_1}\t\t {diagram_2}\t\t {diagram_3}')