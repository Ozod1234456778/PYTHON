

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task.completed else "Pending"
            print(f"{i}. {task.title} - {status} (Due: {task.due_date})")

    def list_incomplete_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            if not task.completed:
                print(f"{i}. {task.title} - (Due: {task.due_date})")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()

# main.py
from task import Task
from todolist import ToDoList

todo = ToDoList()

while True:
    print("\n1. Add Task\n2. Complete Task\n3. List All Tasks\n4. List Incomplete Tasks\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due Date: ")
        todo.add_task(Task(title, description, due_date))
    elif choice == '2':
        todo.list_all_tasks()
        index = int(input("Enter task number to complete: ")) - 1
        todo.complete_task(index)
    elif choice == '3':
        todo.list_all_tasks()
    elif choice == '4':
        todo.list_incomplete_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
Homework 2: Simple Blog System


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for i, post in enumerate(self.posts, 1):
            print(f"{i}. {post.title} by {post.author}\n{post.content}\n")

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"{post.title}\n{post.content}\n")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content

    def latest_posts(self, n=3):
        for post in self.posts[-n:]:
            print(f"{post.title} by {post.author}\n{post.content}\n")

#
from blog import Blog
from post import Post

blog = Blog()

while True:
    print("\n1. Add Post\n2. List All Posts\n3. Posts by Author\n4. Delete Post\n5. Edit Post\n6. Latest Posts\n7. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        title = input("Title: ")
        content = input("Content: ")
        author = input("Author: ")
        blog.add_post(Post(title, content, author))
    elif choice == '2':
        blog.list_all_posts()
    elif choice == '3':
        author = input("Enter author's name: ")
        blog.posts_by_author(author)
    elif choice == '4':
        blog.list_all_posts()
        index = int(input("Enter post number to delete: ")) - 1
        blog.delete_post(index)
    elif choice == '5':
        blog.list_all_posts()
        index = int(input("Enter post number to edit: ")) - 1
        title = input("New Title: ")
        content = input("New Content: ")
        blog.edit_post(index, title, content)
    elif choice == '6':
        blog.latest_posts()
    elif choice == '7':
        break
Homework 3: Simple Banking System


class Account:
    def __init__(self, acc_num, name, balance=0):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient balance.")
            return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_num] = acc

    def find_account(self, acc_num):
        return self.accounts.get(acc_num)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver and sender.withdraw(amount):
            receiver.deposit(amount)
            print("Transfer successful.")
        else:
            print("Transfer failed.")


from bank import Bank
from account import Account

bank = Bank()

while True:
    print("\n1. Add Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        acc_num = input("Account Number: ")
        name = input("Account Holder Name: ")
        bank.add_account(Account(acc_num, name))
    elif choice == '2':
        acc_num = input("Account Number: ")
        acc = bank.find_account(acc_num)
        if acc:
            print(f"Balance: {acc.balance}")
    elif choice == '3':
        acc_num = input("Account Number: ")
        amount = float(input("Amount to deposit: "))
        acc = bank.find_account(acc_num)
        if acc:
            acc.deposit(amount)
    elif choice == '4':
        acc_num = input("Account Number: ")
        amount = float(input("Amount to withdraw: "))
        acc = bank.find_account(acc_num)
        if acc:
            acc.withdraw(amount)
    elif choice == '5':
        from_acc = input("From Account Number: ")
        to_acc = input("To Account Number: ")
        amount = float(input("Amount to transfer: "))
        bank.transfer(from_acc, to_acc, amount)
    elif choice == '6':
        break
