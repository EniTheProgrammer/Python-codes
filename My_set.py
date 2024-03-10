# st=set()
# print(type(st))
# st={}
# print(type(st))
fruit={"Watermelon", "Pear", "Pear", "Orange"}
vegetables={"Spinach", "Tomato", "Pepper", "Cabbage"}
# print(len(fruit))
# print("Pear" in fruit)

# Adding item to a set
# fruit.add("Strawberry")
# print(fruit)

# removing items from a set
# fruit.remove("Watermelon")
# print(fruit)

# clearing a set
# fruit.clear()
# print(fruit)

# deleting a set
# del fruit
# print(fruit)

# converting list to set
# lst=["a", "b", "c"]
# st=set(lst)
# print(st)

# joining set
# Union of set
# food=fruit.union(vegetables)
# print(food)


# Updating a set
# fruit.update(vegetables)
# print(fruit)

# # intersection of sets
# st1={"p", "y", "t", "h", "o", "n"}
# st2={"h", "a", "c", "k", "a", "t", "o", "n"}
# stinter=st1.intersection(st2)
# print(stinter)

# Subset and superset
no1={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
no2={1, 2, 3, 4, 5}
# no3=no1.issubset(no2)
# no3=no1.issuperset(no2)

# checking the difference between two sets 
# no4={0, 1, 2, 3, 4, 11, 12}
# difno=no1.difference(no4)
# difno=no4.difference(no1)
# print(difno)

# Symmetric sets
set_a={1, 2, 3, 4, 5}
set_b={3, 4, 5, 6, 7}
symettric_diff=set_a.symmetric_difference(set_b)
# print(symettric_diff)

# Joining two sets 
set_c={9, 10, 11}
itj=set_a.isdisjoint(set_c)
print(itj)
