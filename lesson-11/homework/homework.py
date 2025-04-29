python -m venv myenv



myenv\Scripts\activate


source myenv/bin/activate

# 3. Install some packages
pip install requests numpy



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)



│
├── __init__.py
└── circle.py
📄 geometry/__init__.py


import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

file_operations/
│
├── __init__.py
├── file_reader.py
└── file_writer.py
📄 file_operations/__init__.py
ь
# file_operations/__init__.py
# Empty or used for imports
📄 file_operations/file_reader.py

# file_operations/file_reader.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:


def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

📄 main.py
from math_operations import add, subtract
from string_utils import reverse_string
from geometry.circle import calculate_area
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

print("Addition:", add(10, 5))
print("Reversed string:", reverse_string("hello"))
print("Circle area (r=5):", calculate_area(5))

write_file("example.txt", "Hello, world!")
print("File content:", read_file("example.txt"))
