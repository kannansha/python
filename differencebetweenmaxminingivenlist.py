n=int(input('Enter the no.of elements:'))
l=list(map(int,input().split()))
max=l[0]
min=max
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
d=max-min
print('difference between max and min given list is',d)
