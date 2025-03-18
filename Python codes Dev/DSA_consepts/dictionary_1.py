#Setting the dictionary
me={
    "name": "Dev",
    "age": 10,
    "country":"India",
    "state": "New Delhi",
    "grade": 5,
    "birthday": "12/2/14"
}
#Print specific values in the dictionary
print(me["country"])
#Printing whole dictionary
print(me)
#Printing only the keys in a dictionary
print(me.keys())
#Printing only the values in the dictionary
print(me.values())
for i in me.keys():
    print(i,me[i])
if "country" in me:
    print(me["country"])
else:
    print("No value named country")
#Adding to the dictionary
me["fav color"]="orange"
print(me["fav color"])
#Deleting values
del me["state"]
print(me)
#changing values
me["age"]=9
print(me)