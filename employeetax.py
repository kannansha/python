empname=input('Employee name:')
emppo=int(input('Employee phone no:'))
bslry=int(input('basic salary:'))
da=int(input('daily allowance'))
ta=int(input('Travel allowance:'))
hra=int(input('House rental allowance:'))
netsalary=bslry+da+ta+hra
if netsalary>100000:
    tax=netsalary*(10/100)
    print('Tax has to pay is',tax)
elif netsalary>50000:
    tax=netsalary*(7/100)
    print('Tax has to pay is',tax)
elif netsalary>40000:
    tax=netsalary*(4/100)
    print('Tax has to pay is',tax)
elif netsalary>20000:
    tax=netsalary*(2/100)
    print('Tax has to pay is',tax)
else:
    print('NO need to pay tax')
