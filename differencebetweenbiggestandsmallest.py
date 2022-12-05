n=int(input("Enter how numbers your want:"))
num=int(input("Enter any number:")) 
largest=num
smallest=num
i=1
while(i<n):
    num=int(input("Enter any number:"))
    if(num>largest):
        largest=num
    if(num<smallest):
        smallest=num
    i=i+1 
print("The largest number is " , largest)
print("The smallest number is ",smallest)
d=largest-smallest
print(d,'is the difference')
