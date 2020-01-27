#! python3
#Determines the strength of a password

import re

def strengthPass(password):
    
    number = re.compile(r'[0-9]+')
    upper = re.compile(r'[A-Z]+')
    lower = re.compile(r'[a-z]')
    
    if number.search(password) == None:
        return False
    elif upper.search(password) == None:
        return False
    elif lower.search(password) == None:
        return False
    elif len(password) < 8:
        return False
    else:
        return True

Password = '12kiNgs3'

if strengthPass(Password):
    print('Good Password')
else:
    print("Password not strong enough")