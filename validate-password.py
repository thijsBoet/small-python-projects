import re

while True:
  password = input('Enter your new password: ')
  if len(password) < 8:
    print('Password must be at least 8 characters.')
    continue
  elif not re.search('[a-z]', password):
    print('Password must contain at least one lowercase character.')
    continue
  elif not re.search('[A-Z]', password):
    print('Password must contain at least one uppercase character.')
    continue
  elif not re.search('[0-9]', password):
    print('Password must be at least one number.')
    continue
  elif not re.search('[$@#%._]', password):
    print('Password must contain one special character \($@#%._\).')
    continue
  elif re.search('\s', password):
    print('Password cannot contain any spaces.')
    continue
  else:
    valPassword = input('Please repeat your password.')
    if password == valPassword:
      print('Thank you for creating a new password')
      break
    else:
      print('Passwords do not match.')
      continue