cphno=input('Enter Customer phone number:')
cname=input('Enter Customer name:')
previous=int(input('Enter previous reading:'))
present=int(input('Enter present reading:'))
units=present-previous
if units<=30:
    bill=units*1.90
elif units<=75:
    s=units-30
    bill=(30*1.90)+(s*3.00)
elif units<=125:
    s=units-75
    bill=(75*3.00)+(s*4.50)
elif units<=225:
    s=units-125
    bill=(125*4.50)+(s*6.00)
elif units<=400:
    s=units-225
    bill=(225*6.00)+(s*8.75)
elif units>400:
    s=units-400
    bill=(400*8.75)+(s*9.75)
print('customer phone no:',cphno)
print('customer name:',cname)
print('Electricity bill:',bill)
