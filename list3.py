n=int(input('Enter the no.of elements:'))
l=list(map(int,input().split( )))
m=[]
for i in l:
    if i not in m:
        m.append(i)
        m.sort(reverse=True)
print(m[1])
