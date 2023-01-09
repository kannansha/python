def sort_dec(l):
    return sorted(l,reverse=True)

s=input()
l=[]
for i in s:
    l.append(int(i))
sd=sort_dec(l)
res=''
for i in sd:
    res=res+str(i)
print(res)
