n=int(input('Enter any value:'))
a=0
b=1
s=0
for i in range(n):
    s += b
    a, b = b, a+b
print(s)
