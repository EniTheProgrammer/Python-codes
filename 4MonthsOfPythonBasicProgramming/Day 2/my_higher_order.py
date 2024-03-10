# Function as a parameter
# def sum_numbers(n):
#     return sum(n)

# def higher_function(f, lst):
#     summation=f(lst)
#     return summation

# result=higher_function(sum_numbers, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(result)

#function as a return value
# def square_numbers(n):
#     return n**2

# def cube_numbers(n):
#     return n**3

# def absolute_of_n(n):
#     if n>= 0:
#         return n
#     else:
#         return (-n)

# def higher_function(type):
#     if type=="square_numbers":
#         return square_numbers
#     elif type=="cube_numbers":
#         return cube_numbers
#     elif type=="absolute_of_n":
#         return absolute_of_n

# result=higher_function("square_numbers")
# result=higher_function("cube_numbers")
# result=higher_function("absolute_of_n")
# print(result(-3))

# Example of closure
# def add_ten():
#     ten=10
#     def add(n):
#         return n+ten
#     return add
# closure_result=add_ten()
# print(closure_result(5))

# decorator
# def greeting():
#     return "coding with python"
# def upper_case_decorator(cool_func):
#     def wrapper():
#         func=cool_func()
#         make_upper_case=func.upper()
#         return make_upper_case
#     return wrapper
# greet=upper_case_decorator(greeting)
# print(greet())

# def upper_case_decorator(cool_func):
#     def wrapper():
#         func=cool_func()
#         make_upper_case=func.upper()
#         return make_upper_case
#     return wrapper
# @upper_case_decorator
# def details():
#     return "eni"
# print(details())

# first decorator
def upper_case_decorator(cool_func):
    def wrapper():
        func=cool_func()
        make_upper_case=func.upper()
        return make_upper_case
    return wrapper

# second decorator 
def split_string_decorator(cool_func):
    def wrapper():
        func=cool_func()
        make_split_string=func.split()
        return make_split_string
    return wrapper
@split_string_decorator
@upper_case_decorator
def movement():
    return "i am walking"
print (movement())

