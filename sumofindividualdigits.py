n=int(input('Enter any value:'))
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print('sum of the individual digits of given number is',s)
