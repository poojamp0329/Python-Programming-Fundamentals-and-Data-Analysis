#functions,global variables and local variables

#functions: resuable block of code that performs a specific task when called

def greet():
    print("hello,Good Morning!")

greet()

#parameter

def marraige(boy,girl):
    print(f"{boy} married {girl}")

marraige("chandan","sneha") #positional arguments
marraige(boy="chandan",girl="priya")#keyword arugments


def tables(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")

tables(2)

#default parameter values

def marraige(boy,girl="girl"):
    print(f"{boy} married {girl}")

marraige("chandan")


#returning values from a function

def func(num):
    return int(str(num)*5)

a=10
c= a+func(2)
print(c)

def func(num):
    return (num)*5

a=10
c= a+func(2)
print(c)


#local and global variables

x="pooja"  #global variable

def func():
    y="priya" #local variable
    print(y)
    print(x) #x is a global variable therefore is accessible inside the function

func()

#print(y) #y is local variable therefore it is not accesible outside the function


#homework

def greet_user(name):
    print(f"hello,{name}")

greet_user("mahesh")
greet_user("mohitha")

def sum(a,b):
    return (a+b)

c=sum(3,5)
print(c)

a=30
c=a+sum(4,56)
print(c)