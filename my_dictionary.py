person={
    "first_name":"Eni",
    "last_name":"Adigun",
    "Age":14,
    "Country":"Nigeria",
    "Student":True,
    "Skills":["Python", "HTML", "JavaScript"],
    "Address":{
        "Street":"Rose",
        "Postcode":"AB10 1UB"
    }
}

# print(len(person))

# Accessing dictionary items
# print(person["first_name"])
# print(person["Skills"][1])
# print(person["City"])

# Checking dictionary with get method
# print(person.get("City"))

# How to add item to dictionary
# person["City"]="Aberdeen"
# print(person)
# person["Skills"].append("script")
# print(person)

# Modifiying items in dictionary
# person["first_name"]="Fikayo"
# print(person)

# Checking keys in dictionary by using in
# print("first_name" in person)

# Removing keys and value pairs from a dictionary
# pop 
# person.pop("first_name")
# print(person)

# popitem
# person.popitem()
# print(person)

# deleting item in a dictionary
# del person["Country"]
# print(person)

# converting a dictionary to list
#Using item to change dictionary to list
# print(person.items())

# clearing a dictionary
# using the clear key word
# print(person.clear())

# copying a dictionary
# new_dict=person.copy()
# print(new_dict)

# getting dictionary keys as a list
# keys=person.keys()
# print(keys)
# getting dictionary values as a list
values=person.values()
print(values)