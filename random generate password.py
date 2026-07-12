import random
import string

length = int(input("enter the length of the passsward :"))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Password:", password)