dict = {"name" : "Shayan", "age" : "13"}

print(dict["name"])

dict["adress"] = "Singapore"
print(dict)
dict["age"] = 14 
print(dict)

print("The adress is :" , dict.get("adress"))

dict.pop("adress")
print(dict)

dict.clear()
print(dict)

