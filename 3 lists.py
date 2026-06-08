#class5
veggies = ["carrot", "tomato", "potato", "onion"]
print(veggies)
print(veggies[0])
print(veggies[-2])
print(veggies[1])

veggies[1]= "chilli"
print(veggies)

veggies.append("tomato")
print(veggies)

veggies.remove("potato")
print(veggies)

print("next")

#veggies.remove[1].cannot be used

veggies.insert(2, "potato")
print(veggies)

veggies.pop()
print(veggies)

veggies.pop(0)
print(veggies)

veggies.pop(1)
print(veggies)

#veggies.insert(0,"carrot": 1, "tomato")
veggies.insert(0,"carrot")
veggies.append("tomato")
print(veggies)

veggies.clear()
print(veggies)

print("slicing of lists")
#slicing
#list_name[start:stop:step]

numb = [5,10,15,20,25,30]
print(numb[0:3])
print(numb[0:])
print(numb[:4])
print(numb[2:5])
print(numb[0::2])
print(numb[0:4:2])

print(len(numb))

number = [4,3,5,2,8,5]
print(sorted(number))
print(number) #original list remain unchanged

print(sum(number))

print(number.index(5)) #it gives position of the input is present in the list
print(number.index(4))
print(number.index(2))

print(numb.index(15))

print(number.count(5))
print(number.count(4))

#print(number.reverse()) output=none

number.reverse()
print(number)

vege =["carrot", "beet", "roots"]
#print(vege.reverse()) it won't work

vege.reverse()
print(vege)

#print(list_name[::-1])(chatgpt)
print(vege[::-1])

number.sort()
print(number)
number.pop(3)
print(number)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print(matrix[0])
print(matrix[0][2])

#hw

my_list = ["banana", 25, "apple",23]
my_list.append("yashu")
print(my_list)
my_list.insert(1,"pooja")
print(my_list)
my_list.insert(2, 45)
print(my_list)

my_list.remove(45)
print(my_list)
my_list.pop(2)
print(my_list)

numericals = [2,5,6,34,65,87,23,54]

numericals.sort()
print(numericals)
print(sorted(numericals))

#to sort in descending order
#numbers.sort(reverse=True)
numericals.sort(reverse=True)
print(numericals)
sorted_numericals = sorted(numericals,reverse=True)
print(sorted_numericals)

