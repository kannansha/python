n=int(input('Enter any value:'))
sum=0
t=n
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==t):
    print('Perfect number')
else:
    print('Not Perfect number')
        
