#Write a password generator in Python. Be creative with how you generate passwords -
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and 
#symbols. The passwords should be random, generating a new password every time the 
#user asks for a new password. 


import random 
import string

def password_generator(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation 
    random_characters = random.sample(characters, length) #spits out a list
    random_password = "".join(random_characters)
    return random_password

print(password_generator()) 








