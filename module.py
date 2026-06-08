#module is same as a code library 

def greetings(name):
    print("hello,"+name)

person1={
    "name":"pooja",
    "age": "23",
    "dept":"Agricultural stats"
}

person2={
    "name":"ruchitha",
    "age":"22",
    "dept":"agricultural economics"
}

import module as md 
md.greetings("pooja")

x=md.person1
print(x)

y=md.person2["age"]
print(y)

import platform
z=platform.system()
print(z)

print(dir(platform)) #dir() function to list all the functions name in the module

print(dir(md))

from module import person2
print(person2["age"])
print(person2)

import datetime 
x=datetime.datetime.now()
print(x)

print(x.strftime("%A"))

import math 

print(pow(2,3))
print(max(2,4,6,10))
print(math.ceil(2.45))
print(math.floor(2.45))
print(math.sqrt(81))
print(abs(-2.3))
print(math.pi)


import camelcase

c = camelcase.CamelCase()
txt = "i am an indian"
print(c.hump(txt))
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)