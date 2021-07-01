# Method-2 :- Iterating list characters over and over again so elements from each four types can be selected

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
    while len(string)<n:
        for i in characters:
            if len(string)==n:
                break
            else:
                string.append(random.choice(i))
    
    random.shuffle(string)
    print(''.join(string))

password(int(input('Enter length for password between 5 to 20: ')))

# OUTPUT:- N%z!p36LD3
