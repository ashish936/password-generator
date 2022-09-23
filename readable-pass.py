import random
import string

wordlist = []
# getting a list of all special characters
special_char = list(string.punctuation)

# open the file
with open("wikipedia-text.txt", 'r') as file:
    data = file.readlines()

# split them in words
for line in data:
    words = line.split()

    # check for the validity of the word
for item in words:
    if len(item) > 5:
        wordlist.append(item.capitalize())

word = random.choice(wordlist)
schar = random.choice(special_char)
# returns int value and 10 and 90 are included
num = str(random.randint(10, 90))

passw = word + schar + num

print(passw)

# checking token
