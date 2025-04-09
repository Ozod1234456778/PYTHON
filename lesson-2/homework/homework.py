1:Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

from datetime import datetime
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
print(f"Hello {name}, you are {age} years old.")

2:
car_names = ["Tesla", "BMW", "Audi", "Ford", "Chevrolet", "Toyota", "Honda"]
txt = 'LMaasleitbtui'
extracted_cars = [car for car in car_names if car.lower() in txt.lower()]
print("Extracted car names:", extracted_cars)

3:
car_names = ["Mazda", "Tesla", "BMW", "Audi", "Ford", "Chevrolet", "Toyota", "Honda"]
txt = 'MsaatmiazD'
extracted_cars = [car for car in car_names if car.lower() in txt.lower()]
print("Extracted car names:", extracted_cars)

4:Extract the residence area from the following text:txt = "I'am John. I am from London"

txt = "I'am John. I am from London"
residence_area = txt.split("from")[1].strip()
print("Residence area:", residence_area)


5:Write a Python program that takes a user input string and prints it in reverse order.

user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)

6:Write a Python program that counts the number of vowels in a given string.
  
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in input_string if char in vowels)
print(f"The number of vowels in the string is: {vowel_count}")

7:Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
max_value = max(numbers)
print(f"The maximum value is: {max_value}")

8:Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("Enter a word: ")
if word == word[::-1]:
  print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
  
  9:Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Enter your email address: ")
email = input("Enter your email address: ")
domain = email.split('@')[1]
print(f"The domain of the email is: {domain}")

10:Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string
password_length = 12
characters = string.ascii_letters + string.digits + string.punctuation
random_password = ''.join(random.choice(characters) for i in range(password_length))
print(f"Generated password: {random_password}")










