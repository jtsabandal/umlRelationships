#Inheritance
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class GraduateStudent(Student):
    def __init__(self, name, age, thesis_topic):
        self.name = name
        self.age = age
        self.thesis_topic = thesis_topic
    
    def __str__(self):
        return(f"The alumni's name is {self.name}, the alumni's age is {self.age}, and the alumni's thesis topic is {self.thesis_topic}.")

Alumni = GraduateStudent("John Doe", 25, "Artificial Intelligence")

print(Alumni)

#Composition
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class School:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def __str__(self):
        return(f"The school's name is {self.name}, and the teacher's name is {self.teacher.name}.")

my_school = School("Greenwood High", Teacher("Mrs. Smith", "Mathematics"))

for teacher in [my_school.teacher]:
    print(f"The teacher's name is {teacher.name}, and the subject they teach is {teacher.subject}.")

#Aggregation
class Course:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"The course {self.name} has been deleted.")

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def __del__(self):
        print(f"The department {self.name} has been deleted.")

Course1 = Course("Computer Science")
Course2 = Course("Mathematics")

mydepartment = Department("Computer Science")
mydepartment.courses.extend([Course1, Course2])
print(f"The department has the following courses: {[course.name for course in mydepartment.courses]}")

print("Deleting the department...")
del mydepartment

print(f"The courses still exist: (Course1, Course2)")

#Association
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"Author: {self.name}, Books: {[book.title for book in self.books]}"

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.add_book(self)

    def __str__(self):
        return f"The book's title is '{self.title}', and the author's name is {self.author.name}."


author1 = Author("George Orwell")
book1 = Book("1984", author1)
book2 = Book("Animal Farm", author1)

print(book1)
print(book2)
print(author1)

#Dependency
class CreditCard:
    def __init__(self, number, holder):
        self.number = number
        self.holder = holder

class PaymentProcessor:
    def process_payment(self, credit_card, amount):
        print(f"Processing payment of ${amount} for {credit_card.holder} using card {credit_card.number}.")


card1 = CreditCard("1234-5678-9876-5432", "Alice")
card2 = CreditCard("9876-5432-1234-5678", "Bob")

processor = PaymentProcessor()
processor.process_payment(card1, 100)
processor.process_payment(card2, 250)


#Realization
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
