import random
import string

'''
names = ["Shubham", "John", "Ashish", "amit"]

print(random.choice(names))  # function to choose random data from diff fields
print(random.randint(10, 100))  # Select a random no btw range
print(random.randint(1000, 9999))  # Creating a random otp
'''

'''
Make a strong password:
    8 char length
    1 upper char
    1 lower char
    1 numeric digit
    1 special symbol
eg: Action@123
'''
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# another way of getting lowercase letters
lower_char = list(string.ascii_lowercase)
num = list(string.digits)
nums = [0, 1, 2, 3, 4]
special_char = list(string.punctuation)

password = random.choice(upper_char) + random.choice(lower_char) + \
    random.choice(num) + random.choice(special_char)

# Now I have to get the password of length of 8

pass_eight_digit = password + random.choice(upper_char) + random.choice(lower_char) + \
    random.choice(num) + random.choice(special_char)

print(pass_eight_digit)
