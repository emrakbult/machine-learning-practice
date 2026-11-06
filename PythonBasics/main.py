a = 10
b = a

a = 20

print(b) # 10

x = 7
y = float(x)

print(x) # 7
print(y) # 7.0

k, l, m = 5, 10, 15
print(k, l, m) # 5 10 15

c = 7
d = 3

print(c / d) # 2.3333...
print(c // d) # 2
print(c % d) # 1

c = -7

print(c // d) # -3

numbers = [10, 20, 30]

numbers[1] = 99
numbers.append(54)

print(numbers) # [10, 99, 30, 54]

coordinates = (10, 20, 30)

print(coordinates[1]) # 20

# coordinates[1] = 99 # TypeError

data = ([1, 2], [3, 4])

data[1].append(5)
print(data) # ([1, 2], [3, 4, 5])

student = {
    "name": "Ali",
    "age": 21,
    "grade": 68
}

print(["grade"]) # 85

student["grade"] = 90
student["city"] = "Ankara"

student.keys()
student.values()
student.items()
student.pop("city")
student.copy()

a = [10, 20]
b = [10, 20]
c = a

print(a == b)  # True
print(a is b)  # False
print(a is c)  # True

# sequence[start:stop:step] stop excluded
numbers = [10, 20, 30, 40, 50]

numbers[1:4]   # [20, 30, 40]
numbers[:3]    # [10, 20, 30]
numbers[2:]    # [30, 40, 50]
numbers[::2]   # [10, 30, 50]
numbers[::-1]  # [50, 40, 30, 20, 10]

text = "MachineLearning"

print(text[0:7])   # Machine
print(text[::-1])  # gninraeLenihcaM

# Shallow Copy
a = [[1, 2], [3, 4]]
b = a.copy()

a[0].append(99)

print(b)
# [[1, 2, 99], [3, 4]]

data = [1, 2, 3]

# Truthiness
if data:
    print("Liste boş değil")

for x in range(1, 8):
    if x == 3:
        continue

    if x == 6:
        break

    print(x)

names = ["Ali", "Ayşe", "Mehmet"]
scores = [80, 95, 70]

for name, score in zip(names, scores):
    print(name, score)

for index, name in enumerate(names):
    print(index, name)

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(10))
print(add_item(20))
print(add_item(30))

# Scope
x = 10

def example():
    x = 20
    print(x)

example()
print(x)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

emp1 = Employee("Ali", 20000)
emp2 = Employee("Ayşe", 25000)

emp1.display()
emp2.display()

employees = [
    Employee("Ali"),
    Employee("Ayşe"),
    Employee("Mehmet")
]

for employee in employees:
    print(employee.name)

class Animal:
    def speak(self):
        print("Ses")

class Dog(Animal):
    def speak(self):
        print("Hav")

dog = Dog()
dog.speak()  # Hav
