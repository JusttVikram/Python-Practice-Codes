import random
import string

character_values = string.ascii_letters + string.digits + string.punctuation

password_length = int(input('Enter the desired length of your password : '))

password = ''

for i in range(password_length):
    random_password = random.choice(character_values)
    password = password + random_password

print(f'Yeh le bhai tera password : {password}')
print('Chal abhi yaad rakhna.')


# # Using List Comprehension
#
# result = "".join(random.choice(character_values) for i in range (password_length))
# print(result)
