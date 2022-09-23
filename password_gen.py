from random import randint

random_number = randint(45, 90)
random_character = chr(random_number)

print(random_character)

word = "substring"
new_word = ""

for letter in word:
    if letter == "s":
        new_word = new_word + "@"
    else:
        new_word = new_word + letter
        
print(new_word)

