# creating list
# lst=list()
# print(lst)
# print(type(lst))
# countries=["Algeria", "Scotland", "New york"]
# print(countries)
# print(len(countries))
lst=["John", 250, True, {"Country":"Nigeria", "City":"Abuja"}]
# print(lst)
# print(lst[0])
# print(lst[3])
# print(lst[-1])
fruit=["Apple", "Banana", "Carrot", "Orange", "Pear", "Watermelon"]
# fruit_1st,fruit_2nd,fruit_3rd,*rest=fruit
# print(fruit_1st)
# print(fruit_2nd)
# print(rest)

# checking items in lists
does_exist="Apple" in fruit
# print(does_exist)

# inserting item into list
fruit.insert(3, "pawpaw")
# print(fruit)

# append
fruit.append("Mango")
# print(fruit)

# remove
fruit.remove("Banana")
# print(fruit)

# pop
fruit.pop(4)
# print(fruit)

# delete
# del fruit[0:3]
# print(fruit)
# del fruit
# print(fruit)

# Clear
# fruit.clear()
# print(fruit)

# Copy
fruit2=fruit.copy()
# print(fruit2)

# joining list
Vegetables=["Lettuce", "Cabbage","Pepper"]
# Using plus operator to join
# Food=Vegetables+fruit
# print(Food)

# Using extend to join
fruit.extend(Vegetables)
# print(fruit)

# count
# Find out how to use count, index, reversed

# Sorting
# fruit.sort(reverse=True)
# print(fruit)

# Reverse
fruit.reverse()
print(fruit)

