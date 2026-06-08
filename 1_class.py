#class3b
print('yashu')
print("hello,world!")

name= input("enter your name:")
age =int(input("enter your age:"))
print("my name is " + name + ".I am " + str(age) + "years old")
print(f"my name is  {name} .I am  {age} years old")


first_name = "pooja"
last_name = " M.P"
print(first_name + last_name)

greeting = "hello yashu "
print(greeting*3)

message = "  hello,yashu "
print(message.strip())
print(message.upper())
print(message.lower())
print(message.replace("yashu","pooja"))

text= "yashaswini"
print(text[0])
print(text[3])
print(text[:8])
print(text[::2])
print(text[::1])

print("yashu \n fool")
print("yashu \t fool")
print("yashu \\fool")#escape

statement = "yashu is a fool"
print(statement.strip())
print(statement.upper())
print(statement.lower())
print(statement.replace(" ","_"))

messages = "how are you?"
print(len(messages))
print(len(messages.replace(" ",""))) #program to print length of the string excluding spaces

print("hello \n world")