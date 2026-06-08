#class6(tuples and sets)

my_tuple = ("tomato","potato","beans")
print(my_tuple)
tuple2 = ("cherry","mango", 2 ,(1,2))
print(tuple2)

print(tuple2[0])


print(tuple2[0:3])
print(tuple2[0::2])

combined_tuple = my_tuple + tuple2
print(combined_tuple)

repeated_tuple = tuple2 * 3
print(repeated_tuple)

print("cherry" in tuple2)
print(tuple2.count(2))
print(len(tuple2))
print(tuple2[1])
print(tuple2.index(2))
print (tuple2.index("mango"))

#tuple2.insert(1,2)
#tuple2.append(23)
#tuple2.remove("mango")
#tuple2.pop()
#tuple2.clear()


#from list to tuple

my_list = [1,"apple", 3 ,[2,4,5],"orange"]
my_tuple = tuple(my_list)
print(my_list)
print(type(my_list))
print(type(my_tuple))

#my_tuple2= tuple(2, 8, 10) tuple expected atmost 1 argument.therefore use brackets
my_tuple2 = tuple((2,3,8,))
print(my_tuple2)

#convert tuple into list to be able to change it 

tuple3 =(22, 23,"mango",(3,4))
list3 = list(tuple3)
print(type(list3))
list3.append("cherry")
print(list3)
list3.pop(1)
print(list3)
tuple3 = tuple(list3)
print(type(tuple3))
print(tuple3)

del tuple3
#print(tuple3) error occurs because tuple3 file no longer exists

#unpacking tuple
fruits= ("apple", "banana", "citrus")
(green, red, yellow)= fruits
print(green) #output=apple
print(yellow)#output=citrus

fruits= ("apple", "banana", "citrus", "strawberry", "peach","pome")
(green, red, *yellow)= fruits #use asterisk if variables is less than the number of values,then values will be assigned to the variable as a list
print(green) 
print(yellow)

(green,*red, yellow)= fruits
print(red)

#loop tuples
tuple5 = ("mango","orange", "papaya")
for x in tuple5:
    print(x)

#Add elements of a tuple to a list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#sets
set8 = {2,43,85,3,21}
print(set8)

set1 = {"mohitha","ruchitha"}
set2 = {"mohitha","pooja"}

my_set = set1 & set2 #intersection
print(my_set)
my_set3 = set1 | set2 #union 
print(my_set3)
my_set4 = set1 - set2 
print(my_set4)

my_set3.add("simmy")
print(my_set3)

my_set3.pop()
print(my_set3)

my_set3.discard("mohitha") # if we want to discard a element from a set without throwing an error if the element isn't found in the lists
print(my_set3)             #we can use discard key word but it can't br used for lists and tuples

my_set3.discard("priya")
print(my_set3)

my_set3.clear()
print(my_set3)

list=[1,45,"mohi","ruchi"]
tuples = tuple(list)
print(type(tuples))

list2 = [1,2,45,23]
sets = set(list2)
print(type(sets))

