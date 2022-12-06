n=int(input('Enter any number:'))
r=0
t=n
while(n!=0):
    r=r*10
    r=r+n%10
    n=n//10
if r==t:
    print('it is palindrome')
else:
    print('it is not palindrome')
