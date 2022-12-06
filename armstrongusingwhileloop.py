n=int(input('Enter any number:'))
s=0
t=n
while(n!=0):
    r=n%10
    s=s+(r*r*r)
    n=n//10
if s==t:
    print('Given number is armstrong')
else:
    print('Given number is not armstrong')
