n1=int(input('Enter the starting value:'))
n2=int(input('Enter the ending value'))
for i in range(n1,n2):
    if((i%4==0) and (i%100!=0)):
        print(i,'is a leap year')
    elif i%400==0:
        print(i,'is a leap year')

