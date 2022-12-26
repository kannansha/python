n=int(input('Enter any positive integer:'))
i=2
f=2
while(i<n):
    if n%i==0:
        f=f+1
        break
    i=i+1
if(f==2):
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')
