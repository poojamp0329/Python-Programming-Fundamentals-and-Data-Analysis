#class4
a = 10
a += 100

print(a)
a *= 10
print(a)

x = 10
y = 5
print(x == y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

print("pooja")
print(x>5 and y<=5)
print(x<5 or y>5)
print (not(x>5 or y>5))

print(1>2 and 2<1)
print(1<2 or 2<1)
print(not(1<2 or 2<1))

print("  \n  ")
list= {1,2,3,4,5,6}
print(3 in list)
print(3 not in list)
print(8 in list)

string = "messages" 
print("m" in string)
print("j" in string)

print("   \n  ")
b = 2
c = 5
print(b & c)
print(b | c)
print(b ^ c)
print(b << c)
print(~b)

y = 5
z = 12
print(z>10 and y>10)
print(z<5 or y<5)
print(not(y>z))

age = int(input("your age="))
if age <= 17:
    print("you are minor")
else:
    print('you are an adult')


word = input("world_ = ")
print('a' in word)
print('python'not in word)

a= 3
b= 4
print(a&b)  
"""AND gate: Y=AB
   OR gate: Y=A+B
   XOR gate : Y=A'B+B'A
"""
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
