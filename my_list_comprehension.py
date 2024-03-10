# syntax for list comprehension
# [i for i in iterable if expression]

num="number"
# lst=list(num)
# print(type(lst))
# print(lst)

# 2nd way of creating list comprehension
# lst=[i for i in num]
# print(lst)

# Generating numbers
# Numbers=[i for i in range(8)]
# print(Numbers)

# square=[i*i for i in range(9)]
# print(square)

# Cube=[i*i*i for i in range(10)]

# second method for cube
# Cube=[i**3 for i in range(10)]
# print(Cube)

# Generating even numbers
# even_no=[i for i in range(21) if i%2==0]

# Generating Odd numbers
# odd_no=[i for i in range(21) if i%2==1]
# print(odd_no)

# list_of_numbers=[-7, -6, -2, 0, 3, 5, 8 ]
# positive_even_numbers=[i for i in range(17) if i%2==0 and i>0]
# print(positive_even_numbers)

# Flattening a 3D list
list_of_lists=[[1, 2, 3], ["Blue", "Yellow", "Red"], ["Sky", "Time", "Monkey"]]
Flattened_list=[item for row in list_of_lists for item in row]
print(Flattened_list)