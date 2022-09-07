import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

totalLetters = int(
    input("How many letters would you like in your password?\n"))

totalSymbols = int(input(f"How many symbols would you like?\n"))

totalNumbers = int(input(f"How many numbers would you like?\n"))

# Method 1 : John@@01
password = ""
for i in range(0, totalLetters):

    password += random.choice(letters)

for j in range(0, totalSymbols):
    password += random.choice(symbols)

for k in range(0, totalNumbers):
    password += random.choice(numbers)

print(password)

# Method 2 : @j1oh@n0
password_list = []
for i in range(0, totalLetters):
    password_list.append(random.choice(letters))

for j in range(0, totalSymbols):
    password_list.append(random.choice(symbols))

for k in range(0, totalNumbers):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)

password2 = ""
for char in password_list:
    password2 += char

print(password2)
