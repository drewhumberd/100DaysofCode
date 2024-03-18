#Password Generator Project
import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_length = nr_letters + nr_symbols + nr_numbers
password = ""
for i in range(0, nr_letters):
  password = password + random.choice(letters) 
for i in range(0, nr_symbols):
  password = password + random.choice(symbols)
for i in range(0, nr_numbers):
  password = password + random.choice(numbers)
print(f"Your password is {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_length = nr_letters + nr_symbols + nr_numbers
password = ""
for i in range(0, nr_letters):
  password = password + random.choice(letters) + " "
for i in range(0, nr_symbols):
  password = password + random.choice(symbols) + " "
for i in range(0, nr_numbers):
  password = password + random.choice(numbers) + " "
password_list = password.split()
random.shuffle(password_list)
password = ""
for i in password_list:
  password = password + i
print(f"Your password is {password}")