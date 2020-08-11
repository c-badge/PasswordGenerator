# using SystemRandom to generate cryptographically secure random numbers
from random import SystemRandom

# lists of character sets
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

# create SystemRandom object
c = SystemRandom()

# ask user for length of password
length = input('Length: ')

# check that the entered length is an integer. exit if not
try:
    int(length)
except ValueError:
    print('\nEnter an integer.\nExiting...')
    exit()

# ask user which character sets to use. uppercase Y or N signifies default choice
l = input('Lowercase? (Y/n) ')
u = input('Uppercase? (Y/n) ')
d = input('Digits? (Y/n) ')
s = input('Symbols? (y/N) ')

# check that at least one character set has been chosen. exit if not
if l.lower() == 'n' and u.lower() == 'n' and d.lower() == 'n' and s.lower() != 'y':
    print('\nChoose at least one character set.\nExiting...')
    exit()

# create list to hold chosen character sets
chars = []

# fill list with chosen character sets
if l.lower() != 'n':
    for letter in lower:
        chars.append(letter)
if u.lower() != 'n':
    for letter in upper:
        chars.append(letter)
if d.lower() != 'n':
    for digit in digits:
        chars.append(digit)
if s.lower() == 'y':
    for symbol in symbols:
        chars.append(symbol)

# create string to hold generated password
pw = ''

# generate password from chosen character sets
for x in range(int(length)):
    pw += chars[c.randint(0, len(chars))]

# print generated password
print('\nPassword: ' + pw)