#object oriented Programming
class Myclass:
    x=5

p1=Myclass()
print(p1.x)

#__init__ function

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("pooja",23)
print(p1.name)
print(p1.age)

#__str__ function 
class person:
    def __init__(abc,name,age):
       abc.name= name
       abc.age=age

    def __str__(abc):
       return f"{abc.name} { abc.age}"
p2=person("yashu",20)
print(p2)

""" self is a parameter refers to current instance, you can use any word but it should 
    be the first paramter in anyfunction of the class"""

#object methods 

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("My name is "+self.name + ".I am "+str(self.age)+" years old")

p3=person("ruchitha",22)
p3.myfunc()

#modifying the object properties
p3.age=24
p3.myfunc()

#delete the oject properties and also object 
"""del p3.age
p3.myfunc()

del p2
print(p2)"""
# you will error in the above two cases

#inheritance :defines a class that inherits all the methods and properties from another class

class student(person):
    pass
s1=student("mohitha",22)
s1.myfunc()

class student(person):
    def __init__(self,name,age,year):
        super().__init__(name,age)  #super() function makes the child class inherit all the methods and properties of parent
        self.year=year

    def func(self):
        print("Myself "+ self.name + "," +str(self.age) + " years old. Graduated on " + str(self.year))

s2=student("pallavi",22,2024)
s2.func()


#iterators

class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a+=1
        return x
    
y=mynumbers()
myiter = iter(y)
print(next(myiter))
print(next(myiter))


class mynumb():
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
        
z=mynumb()
myit=iter(z)
for e in myit:
    print(e)


#polymorphism 

class vehicle:
    def __init__(self,brand,name):
        self.brand=brand
        self.name=name

    def move(self):
        print("move!")

class car(vehicle):
    pass

class ship(vehicle):
    def move(self):
        print("sail!")

class plane(vehicle):
    def move(self):
        print("fly!")

c1= car("hyundai","eon")
s1= ship("tata","arjun")
p1= plane("AirIndia","344")

for x in (c1,s1,p1):
    print(x.brand)
    print(x.name)
    x.move()


     