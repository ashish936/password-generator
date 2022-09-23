import random
import string

wordlist = []
special_char = list(string.punctuation)  # getting a list of all special characters

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
num = str(random.randint(10, 90)) # returns int value and 10 and 90 are included

passw = word + schar + num

print(passw)