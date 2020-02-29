import random
import string

def createRandomPassword(amountOfCharacters):
    chars = list(string.ascii_letters + string.digits)
    password = ''
    for letter in range(amountOfCharacters):
        password += chars[random.randrange(0, len(chars))]

    return password

print(createRandomPassword(32))