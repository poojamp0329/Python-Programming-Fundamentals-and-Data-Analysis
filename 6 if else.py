# if-elif-else



#mohitha
current_mood = input("current mood:")

if current_mood== "happy":
    print("sweet talking")
else:
    if current_mood== "angry":
        print("buy chocolate")
    elif current_mood == "frustrated":
        print("watch blogs")
    elif current_mood== "sad":
        print("act cute")
    elif current_mood == "pain":
        print("console her")
    elif current_mood== "annoyed":
        print("don't talk to her")
    else:
        print("stay away from her")


age= int(input("age:"))

if age<5:
    print("bus fare is free")
elif age>60:
    print("senior citizen discount")
else:
    print("pay the full fare")

time= int(input("time:"))

if time== 8:
    print("time of breakfast")
elif time== 13:
    print("time for lunch")
elif time == 18:
    print("time for dinner")
else:
    print("it's not a meal time")


ages = int(input("age of person:"))

if ages < 18:
    print("student membership")
elif ages>=60:
    print("senior citizen membership")
else:
    print("regular membership")


age3 = int(input("age:"))

if age3<=5 or age3>60:
    print("free ticket")
else:
    print("pay the fare")