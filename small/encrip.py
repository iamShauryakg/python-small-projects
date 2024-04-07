import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars : {chars}")
# print(f"Key : {key}")

#Encript
plain_text = input("Enter a message here to encript: ")
chiper_text = ""

for letter in plain_text:
    index = chars.index(letter)
    chiper_text += key[index]

print(f" original Message {plain_text}")
print(f"Encript_text: {chiper_text}")

#Decript
chiper_text = input("Enter a message here to encript: ")
plain_text = ""

for letter in chiper_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encript_text: {chiper_text}")
print(f" original Message {plain_text}")