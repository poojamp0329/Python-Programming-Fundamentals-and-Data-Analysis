#dicitionary

dict ={
    "mohitha":"mangabilli",
    "ruchitha":"battery",
    "sneha": "simmy"
}

print(dict["mohitha"])
print(dict.get("priya"))

print(dict.get("priya","not found"))

dict["priya"] = "chudail"
print(dict)

dict["ruchitha"]= "ruchi"
print(dict)

frnd_name= dict.pop("priya")
print(frnd_name)

del dict["sneha"]
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())

new_name = {"chitra":"shoki"}
dict.update(new_name)
print(dict)

friend1={
    "name":"ruchitha",
    "fav_sub": "economics",
    "fav_food":"healthy food" 
}

friend2={
    "name": "mohitha",
    "fav_sub": "stats",
    "fav_food" : "biryani"
}

print(friend1["fav_food"],friend2["fav_sub"])

print(friend1["name"],friend1["fav_food"])

#ways to remove the items from the dictionary
friend1.pop("fav_food")
friend2.pop("fav_food")
print(friend1)
print(friend2)

#ways to add items to the dictionary
friend1.update({"food":"dosa"})
print(friend1)

friend2["food"]="pizza"
print(friend2)

del friend2
#print(friend2) this will gives u error beacuse dict is already deleted

del friend1["food"]
print(friend1)

friend1.clear()
print(friend1)