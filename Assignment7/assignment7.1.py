#regex pattern for emails
import re
email="parveenyadavpy57377@gmail.com"
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern,email):
    print("valid email")
else:
    print("invalid email")


#regex pattern for mobile number

mobile="7374951161"
pattern=r'^[6-9]\d{9}$'

if re.match(pattern,mobile):
    print("VALID MOBILE NUMBER")
else:
    print("INVALID")


#regex pattern for date

date='2027-03-10'
pattern=r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-\d{4}$'

if re.match(pattern,date):
    print("valid date")
else:
    print("invalid")