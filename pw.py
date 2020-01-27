#! python3
# An insecure password locker program
PASSWORDS = {'email': 'bmnsi2nci4ovno4ns9nkv',
             'blog': '3nkn4nrkn9nv84knk9ckbv',
             'luggage': '1234'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]   #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print("There's no account named " +account)