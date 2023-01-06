email = input('EMAIL :')
phno = input('MOBILE NUMBER :')
if email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@adc.aditya.ac.in") and len(phno) == 10:
     print("Registration succesfully")
else:
     print("Check your details")
