# Method-1:- Randomly choosing 1st four elements from each types
import random

print('Minimum length of password should be 5 characters')
print('Maximum length of password should be 20 characters')

num=[str(i) for i in range(10)]
upper=[chr(i) for i in range(65,91)]
lower=[chr(i) for i in range(97,123)]
symbol=['@','#','$','%','^','&','*','!']
characters=[num,upper,lower,symbol]

'''
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

['@', '#', '$', '%', '^', '&', '*', '!']
'''

def password(n):
    string=[]
    string.append(random.choice(num))   # Atleast 1 number
    string.append(random.choice(upper))     # Atleast 1 upper case
    string.append(random.choice(lower))     # Atleast 1 lower case
    string.append(random.choice(symbol))   # Atleast 1 symbol

    for i in range((n-len(string))): # Because (n-len(string)) places are already filled by conditional characters
        a = random.choice(random.choice(characters))
        string.append(a)
    random.shuffle(string)
    print(''.join(string))

password(int(input('Enter length for password between 5 to 20: ')))

# OUTPUT:- CE3#7cIB5*
