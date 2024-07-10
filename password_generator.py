import random

uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase= uppercase.lower()
Digits= "0123456789"
Symbols= "(){}<>?/:;[]&%$#@-+*!"

upper,lower,nums,syms = True,True,True,True

all=""

if upper:
    all += uppercase
if lower:
    all += lowercase
if nums:
    all += Digits
if syms :
    all += Symbols

length=20
amount=10

for x in range(amount):
    password= "".join(random.sample(all,length))
    print(password)