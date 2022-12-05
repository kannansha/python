def prime(n):
    i=1
    f=0
    while(range(i,n)):
        if n%i==0:
            f=f+1
        i=i+1
    if f==1:
        return 1
    else:
        return 0

n1=1
n2=int(input('Enter the range:'))
while(range(n1,n2)):
    if(prime(n1)==1):
        print(n1,end='\n')
    n1=n1+1;
