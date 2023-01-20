s=input()
n=len(s)
res=''
for i in range(1,n):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or  s[i]=='O' or s[i]=='U':
        continue
    else:
        res=res+s[i]
print(res)
