sno=int(input('Enter sno.'))
name=input('Enter your name:')
group=input('Enter group name:')
s1=int(input('Enter maths marks:'))
s2=int(input('Enter staistics marks:'))
s3=int(input('Enter computer science marks:'))
print('sno:',sno)
print('name:',name)
print('group:',group)
if s1>=35 and s2>=35 and s3>=35:
    print('PASS')
else:
    print('FAIL')
