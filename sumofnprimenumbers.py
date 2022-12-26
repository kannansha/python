n1=1
n2=int(input('Enter the range:'))
sum=0
while(n1<n2):
    i=1
    f=0
    while(i<n1):
        if n1%i==0:
            f=f+1
        i=i+1
    if f==1:
        sum=sum+n1
    n1=n1+1
print(sum)
