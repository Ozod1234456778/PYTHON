import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


2. Person Class

from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
    
    def age(self):
        today = datetime.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


3. Calculator Class

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


4. Shape and Subclasses

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side


5. Binary Search Tree Class

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)


6. Stack Data Structure

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"


7. Linked List Data Structure
ь
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


8. Shopping Cart Class

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def remove_item(self, item):
        self.items = [i for i in self.items if i[0] != item]
    
    def total_price(self):
        return sum([price for item, price in self.items])


9. Stack with Display

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def display(self):
        if not self.is_empty():
            print("Stack:", self.stack)
        else:
            print("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0


10. Queue Data Structure

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0



11. Bank Class

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id, initial_balance=0):
        self.accounts[account_id] = initial_balance
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id] += amount
        else:
            print("Account not found.")
    
    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            if self.accounts[account_id] >= amount:
                self.accounts[account_id] -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")
    
    def balance(self, account_id):
        return self.accounts.get(account_id, "Account not found.")

