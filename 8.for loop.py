#for loop 

cities = ["hassan","mumbai","bangalore","chennai"]
for city in cities:
    print(city)

l = [23,45,89,10]
for num in l:
    print(num)

for x in range(2,10):
    print(x)

for m in range(1,20,2):
    print(m)

name = "pooja"
for letters in name:
    print(letters)

#enumerate:[(0,"p"),(1,"o"),(2,"o").......]
z = "poojamp"
for index,letter in enumerate(z):
    print(letter * (index+1))

sets= [2,3,4,5]
for index,numbers in enumerate(sets):
    print(f"{numbers} is in {index}th index")
    print(numbers * index)

for numbers in sets:
    print(numbers)
else:
    print("all printed")

for numbers in sets:
    print(numbers)
    if numbers==4:
        break
else:
    print("all printed")

#using for loop for dictionaries

dict = {
    "name": "mohitha",
    "age": 22,
    "income":0
}

for key,value in dict.items():# .items() coverts the dictioners into list of tuples
    print(key, value )

#netsed loops

for i in range(1,11):
    print(f"2 x {i} = {2*i}")

for c in range (2,21):
    for z in range(1,11):
        print(f"{c}x{z} = {z*c}")
    print("")# to print an empty line after each table

cities2 = ["mangaluru ","hassan ","karwar ","mysore "]

for city2 in cities2:
    if city2== "banglore":
        print(f"found {city2}!")
        break
    else:
        print(city2)

print("\n")

for city2 in cities2:
    if city2 == "karwar ":
        print(f"found {city2}!")
        continue
    else:
        print(city2)
   
for index, city in enumerate(cities):
    print(city * (index+1))

for city in cities:
    print(city)
else:
    print("no more cities!")

tickets = 5
passengers =[1,2,3,4,5,6]
for passenger in passengers:
    if tickets>0:
        print("ticket is booked")
        tickets -=1
    else:
        print("all tickets are booked")


#hw  

for num in range(1,30):
    if num%3 ==0:
        print(num)


name = input("enter your name:")
for letter in name:
    print(letters)        
   

total = 0
for num in range(1,11):
    print(total)
    total = total+num
print(total)




for i in range(1,4):
    print("* "*i)
    for j in range(3,0,-1):
        print("* "*j)