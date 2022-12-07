n=int(input('Enter the number:'))
f=1
s=0
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+f
print('sum of given factorial',n,'is',s)
        
