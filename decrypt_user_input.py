# Assignment 2 Problem 2

# Let user input encrypted text
encrypt_input = ("Enter sentence you need to decrypt: ")
# Evaluate encrypted text
for i in range(len(encrypt_input)):
#   if input text encrypted by * change a
    if encrypt_input[i] == "*" :
        encrypted += "a"
#   if input text encrypted by & change e
    elif encrypt_input[i] == "&" :
        encrypted += "e"
#   if input text encrypted by # change i
    elif encrypt_input[i] == "#" :
        encrypted += "i"
#   if input text encrypted by + change o
    elif encrypt_input[i] == "+" :
        encrypted += "o"
#   if input text encrypted by ! change u
    elif encrypt_input[i] == "!" :
        encrypted += "u"
# display decrypted