str=input("Enter any string:")
n=len(str)
c=0
for i in range(0,n):
    if str[i].isalpha()==1:
        c=c+1
print("No of alphabets=",c)
