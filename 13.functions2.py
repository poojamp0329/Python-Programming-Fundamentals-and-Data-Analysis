#advanced concepts of function 

#keyword arguments 

def details(name,age):
    print(f"{name}'s age is {age}")

details(name="pooja",age="22")


#variable length arguments

def add(*num):
    return sum(num)

print(add(1,2,3))

def total_sum(*number):
    total=0
    for num in number:
        total += num
    return total

print(total_sum(1,2,3,4))

def students_details(**details):
    for key,value in details.items():
        print(f"{key}:{value}")

print(type(students_details))

#lambda functions

add=lambda a,b:a+b
print(add(2,3))

double=lambda x:x*2
print(double(5))

students =[
    {"name":"X","age": 22,"percent":90},
    {"name":"Y","age": 24,"percent":85},
    {"name":"Z","age": 23,"percent":67}
]

students.sort(key=lambda x:x["age"],reverse=True)
print(students)

students.sort(key=lambda y:y["percent"])
print(students)

#recursion

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

import math
print(math.factorial(5))

#nested functions

def calculation(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mult():
        print(a*b)
    add()
    sub()
    mult()

calculation(2,1)

#hw
print("Homework")

mult = lambda a,b:a*b
print(mult(2,3))


#sum of first n numbers
def add(n):
    if n==0:
        return 0
    return n+add(n-1)

print(add(5))

#sum of first square natural numbers
def add(n):
    if n==0:
        return 0
    return n**2+add(n-1)

print(add(3))

def avg(*num):
    if len(num)==0:
        return 0
    return sum(num)/len(num)

print(avg(1,2,3,4,5,7,6,5))
