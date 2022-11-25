list=[2,7,12,4,1,5,9]
i=list[0]
sum=0
for i in list:
    if i%2==0:
        sum=sum+i
print('sum of all even numbers in the list is',sum)
