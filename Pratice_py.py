# ### Python Topics with Sample Commands

# | **Topic**                                | **Sample Commands**                                    |
# |------------------------------------------|-------------------------------------------------------|
# | **1. Introduction to Python**           | `print("Hello, World!")`                            |
# | **2. Basic Syntax, Comments, Indentation** | `# This is a comment`                               |
# | **3. Data Types and Variables**         | `a = 5` <br> `fruits = ["apple", "banana"]`        |
# | **4. Basic Operators**                   | `result = a + b` <br> `is_equal = (a == b)`        |
# | **5. Control Structures**                | `if a > b:` <br> `for fruit in fruits:`            |
# | **6. Functions**                         | `def add(x, y): return x + y`                      |
# | **7. Basic Input and Output**           | `name = input("Enter your name: ")` <br> `print(name)` |
# | **8. Data Structures**                   | `numbers = [1, 2, 3]` <br> `squared = {x: x**2 for x in numbers}` |
# | **9. Error Handling**                    | `try: ... except ZeroDivisionError: ...`          |
# | **10. Modules and Packages**             | `import math` <br> `pip install requests`          |
# | **11. Object-Oriented Programming (OOP)** | `class Animal: ...` <br> `dog = Dog("Buddy")`     |
# | **12. Decorators and Generators**       | `@decorator_function` <br> `yield n`              |
# | **13. Basic Algorithms and Problem Solving** | `def bubble_sort(arr): ...`                         |
# | **14. Advanced OOP Concepts**           | `def __str__(self): ...`                           |
# | **15. Functional Programming**           | `result = apply_function(lambda x: x * 2, 5)`     |
# | **16. Concurrency and Parallelism**     | `thread = threading.Thread(target=print_numbers)`  |
# | **17. Working with APIs**                | `response = requests.get('https://api.github.com')` |
# | **18. Database Interaction**             | `conn = sqlite3.connect('example.db')`            |
# | **19. Testing and Debugging**           | `class TestMathMethods(unittest.TestCase): ...`    |
# | **20. Web Development Basics**          | `@app.route('/')` <br> `app.run(debug=True)`      |
# | **21. Data Science and Visualization**   | `df.plot(kind='bar')` <br> `plt.show()`           |
# | **22. Machine Learning Basics**         | `model.fit(X_train, y_train)`                      |
# | **23. Advanced Libraries and Frameworks** | `soup = BeautifulSoup(response.text, 'html.parser')` |

# 1. Introduction to Python
print("Hello, World!")

# 2. Basic Syntax, Comments, Indentation
# This is a comment

# 3. Data Types and Variables
a = 5
b = 3.14
name = "Alice"
fruits = ["apple", "banana", "cherry"]
coordinates = (10.0, 20.0)
person = {"name": "Alice", "age": 30}
unique_numbers = {1, 2, 3, 4}

# 4. Basic Operators
result = a + b
is_equal = (a == b)
is_true = (a > 0 and b < 5)

# 5. Control Structures
if a > b:
    print("a is greater")
elif a < b:
    print("b is greater")
else:
    print("Both are equal")

for fruit in fruits:
    print(fruit)

while a > 0:
    print(a)
    a -= 1

# 6. Functions
def add(x, y):
    return x + y

result = add(5, 3)
print(result)

# 7. Basic Input and Output
name = input("Enter your name: ")
print(f"Hello, {name}!")

# File handling
with open('example.txt', 'w') as f:
    f.write("Hello, World!")

with open('example.txt', 'r') as f:
    content = f.read()
    print(content)

# 8. Data Structures
numbers = [1, 2, 3, 4, 5]
unique_items = set(numbers)
squared = {x: x**2 for x in numbers}

# 9. Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always executes.")

# 10. Modules and Packages
import math
print(math.sqrt(16))

# Create a module (my_module.py)
# def greet(name):
#     return f"Hello, {name}"

# Using pip to install packages
# pip install requests

# 11. Object-Oriented Programming (OOP)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())

# 12. Decorators and Generators
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function executed."

print(display())

# Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)

# 13. Basic Algorithms and Problem Solving
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 2, 9, 1, 5, 6]))

# 14. Advanced OOP Concepts
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
print(p1)

# 15. Functional Programming
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * 2, 5)
print(result)

# Using map, filter, and reduce
from functools import reduce

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

total = reduce(lambda x, y: x + y, numbers)
print(total)

# 16. Concurrency and Parallelism
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# 17. Working with APIs
import requests

response = requests.get('https://api.github.com')
print(response.json())

# 18. Database Interaction
import sqlite3

# Connect to a database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')

# Insert a row of data
c.execute("INSERT INTO users (name) VALUES ('Alice')")

# Save (commit) the changes
conn.commit()

# Query the database
for row in c.execute('SELECT * FROM users'):
    print(row)

conn.close()

# 19. Testing and Debugging
import unittest

def add(a, b):
    return a + b

class TestMathMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

# 20. Web Development Basics
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

# 21. Data Science and Visualization
import pandas as pd
import matplotlib.pyplot as plt

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

df.plot(kind='bar')
plt.show()

# 22. Machine Learning Basics
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print(predictions)

# 23. Advanced Libraries and Frameworks
import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)
