sno=int(input('Enter sno:'))
sn=input('Enter student name:')
group=input('Enter group name:')
s1=int(input('Enter maths marks:'))
s2=int(input('Enter statistics marks:'))
s3=int(input('Enter computer science marks:'))
if s1>=35:
    if s2>=35:
        if s3>=35:
            print('PASS')
if s1<35 or s2<35 or s3<35:
    print('FAIL')
