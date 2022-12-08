m=int(input('Enter the row value:'))
n=int(input('Enter the column value:'))
for i in range(m,0,-1):
    for j in range(1,i+1,1):
        print('*',end='')
    print( )
