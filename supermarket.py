#supermarket
tomatoes=80
potatoes=45
onions=60
brinjal=40
cucumber=50
cphno=input('Enter Customer phone number:')
cname=input('Enter Customer name:')
caddr=input('Enter customer address:')
tomatoes1=int(input('How many kilos of tomatoes you want:'))
potatoes1=int(input('How many kilos of potatoes you want:'))
onions1=int(input('How many kilos of onions you want:'))
brinjal1=int(input('How many kilos of brinjal you want:'))
cucumber1=int(input('How many cucumbers you want:'))
bill=(tomatoes*tomatoes1)+(potatoes*potatoes1)+(onions*onions1)+(brinjal*brinjal1)+(cucumber*cucumber1)
if bill>3000:
    tax=bill*(5/100)
elif bill>2000:
    tax=bill*(7/100)
elif bill>1000:
     tax=bill*(10/100)
elif bill>500:
     tax=bill*(15/100)
else:
    tax=100
bill=tax+bill
print('customer phone no:',cphno)
print('customer name:',cname)
print('tax has to pay is',tax)
print('total bill is',bill)
