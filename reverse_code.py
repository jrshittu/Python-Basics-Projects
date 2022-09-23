# Assign your string
string = "Hello holla hallo oops"

# split the string 
str = string.split()[::-1]

# create an empty list
new_text = []

# iterate through the str and append the it to the empty list created
for i in str:
    new_text.append(i)
 
# prinnt an blank space and join the new_text to it
print(" ".join(new_text))