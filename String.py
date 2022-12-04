'''name = "John Smith"
age = 20
is_new = True'''
'''name = input('What is your name')
print('hi ' + name)'''
'''from turtle import color


name = input('What is your name')
colour = input('What is your favourite colour')
print(name + 'likes' + colour)'''
'''birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)'''

'''weight_lbs = input('Weight (lbs): ')
weight_kg = weight_lbs * 0.45
print(weight_kg)'''
'''course = 'Python for Beginners'
print(course[:5])'''
'''name = 'Jennefer'
print(name[1:-1])'''
'''first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)'''
'''course = 'Pyhton for Beginners'
print(course.upper())
print(course.lower())
print(course)'''
'''course = 'Pyhton for Beginners'
print('Python' in course)'''
'''print(10**3)'''        #arthematic operations
'''x = 10 + 3 * 2 ** 2
print(x)'''
'''x = (2+3) * 10 - 3
print(x)'''
'''import math


print(math.floor(2.9))'''
                                                      #if,elif.else statement
'''is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink pleanty of water")  
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:    
    print("It's a lovely day")  

print("Enjoy your days")'''
'''price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")'''
'''has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")'''
'''temperature = 30

if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day ")'''
                                                #comparision operator
'''name = "J0hn"

if len(name) < 3:
    print("Name must be atleast 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")'''    
                                         #Weight converter
from configparser import ConverterMapping
from sqlite3 import converters
from turtle import colormode


'''weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    connverted = weight / 0.45
    print(f"You are {converted} pounds")'''
                                        #While loops
'''i = 1
while i <=5:
    print('*' * i)
    i = i + 1
print("Done")'''
'''secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Sorry , you failed!")'''
                                     #for loops
'''for item in range(5, 10, 2):
    print(item)'''
'''prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")'''
                             #nested loops
'''for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')'''
'''numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output+= 'x'
    print(output)'''
                          # lists
'''names = ['prithvi', 'bob', 'rock', 'babe']
print(names[2:])
print(names)'''
'''numbers = [3, 12, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)'''
'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for row in matrix:
    for item in row:
        print(item)'''
                 # list methods
'''numbers = [5, 2, 1, 7, 4]
numbers.append(3)
print(numbers)'''
                  # Truples
'''numbers = (1, 2, 3)
print(numbers[0])'''
                 #unpacking truples
'''coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)'''
             #Dictionaries
'''customer = {
    "name": "Prithvi Raj",
    "age": 19,
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])'''
'''phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!")
print(output)'''
        #emoji converter
'''message = input(">")
words = message.split(' ')
print(words)'''
                 #Functions
def greet_user():
    print('hi there!')
    print('Welcome abroad')
    







  


