a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
c=int(input('Enter c value:'))
d=int(input('Enter d value:'))
if a>b:
    if a>c:
        if a>d:
            print('a is big')
if b>c:
    if b<d:
        if b>a:
            print('b is big')
if c>d:
    if c>a:
        if c>b:
            print('c is big')
if d>a:
    if d>b:
        if d>c:
            print('d is big')

