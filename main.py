import random
# lists for letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Python Password Generator.")

#taking inputs
no_letters=int(input("How many letters would you like? \n"))
no_numbers=int(input("How many numbers would you like? \n"))
no_symbols=int(input("How many symbols would you like? \n"))


#generating random password of given size
password=[]
for number in range(no_letters):
  password.append(random.choice(numbers))
for number in range(no_numbers):
  password.append(random.choice(numbers))
for number in range(no_symbols):
  password.append(random.choice(symbols))

#shuffle the password
random.shuffle(password)

#convert list to string and print the fully randomized password
final_pw=""
for key in password:
  final_pw+=key
print(f"Here is your password: {final_pw}")