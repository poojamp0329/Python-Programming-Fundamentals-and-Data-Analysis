#while loop

condition = True
i=1
while condition and i<=20:
    print(f"yes{i}")
    i+=1

sheep_count = 1
while sheep_count<=10:
    print(f"sheep{sheep_count}")
    sheep_count +=1

sheepcount= True
h=1
while sheepcount and h<=15:
    print(f"sheep{h}")
    h+=1

i=1
while i<=5:
    print(i)
    i+=1

sheeps_count = 1
while sheeps_count <=10:
    print(f"sheep{sheeps_count}")
    if sheeps_count==5:
        print("that's enough")
        break
    sheeps_count+=1

is_failed = True
i =1

while is_failed and i<=10:
    if i%2 !=0:
        i +=1
        continue
    print(F"attempt{i}")
    i +=1

     
sheepcount2 = 1
while sheepcount2 <= 5:
    if sheepcount2 == 4:
        sheepcount2+=1
        continue
    print(f"sheep{sheepcount2}")
    sheepcount2 +=1


pin = ""
correct_pin = "1234"
while pin != correct_pin:
    pin = input("enter your pin:")
    if pin != correct_pin:
        print("incorrect pin.try again")
print("correct.proceed")


seats_available = 1
while seats_available >0:
    print(f"available seats{seats_available}")
    booking = input("Do you want to Book a seat?(yes/no):")
    if booking == "yes":
        seats_available-=1
        print("seat is booked")
    else:
        print("no seat is booked")

print("all seats are booked")

snacks_available= 1
money =10

while snacks_available >0 and money>0:
    print(f"available snacks{snacks_available} and money Rs{money}")
    buy = input("do you want buy a snack of worth Rs10?(yes/no):")
    if buy == "yes" and money>0:
        snacks_available-=1
        money-=10
        print("snack is purchased")
    else:
        print("no purchase")
print("Sold out!".upper())


#hw

a =1
while a<=10:
    print(a)
    a+=1

b =1
while b<=20:
    if b%2 ==0:
        b += 1
        continue
    print(b)
    b+=1


seats_present = 1
while seats_present>0:
    print(f"number of seats available are{seats_present}")
    book = input("Do you wish to book a seat?(S/No):")
    if book == "S":
        print("your seat is booked")
        seats_present-=1
    else:
        print("no seat booked")
print("all seats are booked")


c = 10
while c>0:
    print(c)
    c-=1
print("happy new year!".upper())
   
        

pin_number = ""
correct_pin_number = "6789"
x=1
while x<=3:
    pin_number = input(f"x-{x}.Enter your pin number:")
    x+=1
    if pin_number==correct_pin_number:
        print("correct")
        break
    else:
        print("incorrect")

#while in while

i = 0
while i<=10:
    print("pooja "*i)
    i+=1

m =0 
while m <=10:
    l = 0
    while l<m:
        print("pooja", end="")
        l+=1
    print("")
    m+=1






        

    
