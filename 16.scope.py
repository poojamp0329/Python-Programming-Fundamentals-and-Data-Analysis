#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
    
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

y = "pooja"
def myfunc():
   y = "yashu"
   print("hello " + y)
myfunc()
print("hello " + y)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#nonlocal is a keyword makes the variable belong to the outer function ,it is used for the variables inside the nested function
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
