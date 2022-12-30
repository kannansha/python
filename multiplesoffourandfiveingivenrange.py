print("Enter range:")
r=int(input())
l=[i for i in range(1,r+1) if i%4==0 and i%5==0]
print("Multiples of 4 and 5 in this range are:")
print(l)
