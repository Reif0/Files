import random
password = []
chars = "wwertyuioplkjhgfdsazxcvbnm"
symbols = "!@#$%^&*()"
numbers = "1234567890"
for i in range(4):
    password.append(random.choice(numbers))
for i in range(2):
    password.append(random.choice(chars))
    password.append(random.choice(symbols))

final_password = ""
for i in range(len(password)):
    curent_char = random.choice(password)
    final_password += curent_char
    password.remove(curent_char)

print(final_password)

