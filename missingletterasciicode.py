s=input()
s=sorted(s)
n=len(s)
for i in range(1,n):
    if ord(s[i])-ord(s[i-1])==1:
        continue
    else:
        ch=ord(s[i])-1
print(ch)
