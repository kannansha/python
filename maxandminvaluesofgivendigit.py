n=int(input('Enter any value:'))
r=n%10
min=r
max=min
n=n//10
while(n!=0):
    r=n%10
    if(r>max):
        max=r
    if(r<min):
        min=r
    n=n//10
print('Maximum number of the given digit:',max)
print('Minimum number of the given digit:',min)
