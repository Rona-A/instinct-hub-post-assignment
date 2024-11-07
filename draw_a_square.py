row = int(input('Enter number of rows: '))
column = int(input('Enter number of columns:'))
for i in range(0, row):
    for j in range(0, column):
        if (i == 0 or i == (row-1)) or (j == 0 or j == (column-1)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 
