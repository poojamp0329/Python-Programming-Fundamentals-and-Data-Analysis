l = [5,10,15,20]
total = 0
for num in l:
    print(total)
    total = total+num
print(total)

#doubling
l = [4,5,6,7,8,9]
dl=[]
for num in l :
    dl.append(num*2) 
print(dl)

foods=["idli","dosa","vada","poori","rice bath"]
for food in foods:
    print(f"I like {food}")

#dictionaries
student_marks = {
    "ruchitha": 89,
    "mohitha":92,
    "sneha":85
}
    
for students in student_marks:
    print(students)

for students in student_marks.keys():
    print(students)

for marks in student_marks.values():
    print(marks)

     #key,value
for students,marks in student_marks.items():
    print(f"{students} - {marks}")

#ranges can be used in lists

students = ["Sneha","Chithra","Nishu"]
marks = [99,95,97]
student_marks = {}
for index,student in enumerate(students):
    student_marks[student]= marks[index]
print(student_marks)

students = ["Sneha","Chithra","Nishu"]
marks = [99,95,97]
student_marks = {}
for i in range(3):
    student_marks[students[i]]=marks[i]
print(student_marks)

students = ["Sneha","Chithra","Nishu"]
marks = [99,95,97]
student_marks = {}
for i in range(len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)

students = ["Sneha","Chithra","Nishu"]
marks = [99,95,97]
student_marks = {}
for i in range(1,len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)

students = ["Sneha","Chithra","Nishu"]
marks = [99,95,97]
student_marks = {}
for i in range(1,len(students),2):
    student_marks[students[i]]=marks[i]
print(student_marks)

#list comprehension
#1.list comprehension for lists

#new list = [expression for item in collection if condition]

l = [2,4,8,16,32]
dl=[num*2 for num in l]
print(dl)

m = [x for x in range(1,11)]
dm = [num**2 for num in m]
print(dm)

s = [1,2,3,4,5,6,7,8,9,10]
edl = [number**2 for number in s if number%2==0]
print(edl)

names = ["mohitha","ruchitha","sneha"]
uppercased_names= [name.upper() for name in names]
print(uppercased_names)

#list compreehension for dictionaries

#new_dict = {key_expression:value_expression for item in iterable if condition}

numericals = [1,2,32,45]
squared_numericals = {numer:numer**2 for numer in numericals}
print(squared_numericals)

names = ["pooja","preethi","pallavi"]
name_lenghts = {name:len(name) for name in names }
print(name_lenghts)

class_population= {
    "economics": 12,
    "statistics": 6,
    "bioinformatics":2,
    "extension": 14,
    "ABM":20
}

large_population_class ={school:population for school, population in class_population.items() if population>10}
print(large_population_class)

#string.split(separator,maxsplit)

sentence = "I love sweets"
words = sentence.split()
print(words)

sentence2 ="I-hate-poori"
words2 = sentence2.split("-")
print(words2)

data = "apple,banana,orange,mango"
datas = data.split(",")
print(datas)

sent = "python is fun to learn"
sente = sent.split(" ",3)
print(sente)


#hw

foods = ["dosa","idli","vade","paysa"]
uppercased_foods =[food.upper() for food in foods]
print(uppercased_foods)

items_prices ={
    "shoes":2000,
    "polish":200,
    "books": 250,
    "pens": 50
}

total_price = 0
for prices in items_prices.values():
    print(total_price)
    total_price += prices
print(total_price)
#or use
print(sum(list(items_prices.values())))

information =[{"name":"ruchitha","age":22,"marks":90},
              {"name":"mohitha","age":21,"marks":92},
              {"name":"sneha","age":20,"marks":93}]

for student in information:
    print("student information:")
    print(f"Name:{student['name']} \n Age: {student['age']} \n Marks: {student['marks']}")
    print("")


city_popu = {
    "bengaluru": 2000000,
    "mysuru": 1000000,
    "hassan":30000,
    "shivamogga":50000
}

large_cities ={city:popu for city, popu in city_popu.items() if popu>1000000}
print(large_cities)


rows=int(input("enter the number of rows:"))

matrix=[]

for i in range(rows):
    row=[int(num) for num in input(f"enterrow{i+1}:").split()]
    matrix.append(row)
print(matrix)


rows=int(input("enter the number of rows:"))
columns=int(input("enter the number of columns:"))

matrices = []

for i in range(rows):
    row = []
    for j in range(columns):
        x= int(input("enter the element:"))
        row.append(x)
    matrices.append(row)

print(matrices)#doubts need to be clarified