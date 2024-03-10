# def greet():
#     print("Hello world")

# greet()

# def generate_fullname():
#     firstname="Eniola"
#     lastname="Adigun"
#     space=" "
#     fullname=firstname+space+lastname
#     print(fullname)

# generate_fullname()

# def sum_of_nos():
#     no1=3
#     no2=5
#     no3=7
#     sum=no1+no2+no3
#     return sum 

# print(sum_of_nos())

# parameters
# def generate_fullname(firstname, lastname, space):
#      fullname=firstname+space+lastname
#      return fullname
# print (generate_fullname("Eni", " ", "Adigun"))

# def add_ten(number):
#     ten=10
#     return number+ten
# print(add_ten(7))
# print(add_ten(12))

# def power_two(number):
#     square=number*number
#     return square
# print(power_two(4))
# print(power_two(9))

# def area__of_a_circle(radius):
#     pi=3.14
#     area=pi*radius**2
#     return area
# print(area__of_a_circle(14))

# def sum_of_two_nos(number1, number2):
#     sum=number1+number2
#     return sum
# print(sum_of_two_nos(5, 7))

# def age_calculator(year_currently, year_of_birth):
#     age=year_currently-year_of_birth
#     return age
# print(age_calculator(2024, 2009))

# def even_number_detector(number):
#     if number%2==0:
#         print("Even")
#         return True
#     else:
#         print("Even")
#         return False
# print(even_number_detector(6))
# print(even_number_detector(11))

# Functions involving list
# def find_even_numbers(numbers):
#     even=[]
#     for i in range(numbers + 1):
#         if i%2==0:
#             even.append(i)
#     return even
# print(find_even_numbers(10))

# Function with default parameters
# def greetings(name="Eni"):
#     message=name + ", You are under arrest"
#     return message
# print(greetings("Johnny"))
# print(greetings())

# def subscription(name="Customer", account_balance="0"):
#     message="Dear " + name + ", your subscription to our service remains " + account_balance + " units"
#     return message
# print(subscription("Nigerian", "0"))   

# abitrary number of arguments
# def sum_of_numbers(*nos):
#     total=0
#     for n in nos:
#         total +=n
#     return total
# print(sum_of_numbers(2, 4, 6, 7, 9, 3))

# default and abitrary number of parameters
# def generate_team(team, *teams):
#     for i in teams:
#         print(i)
# print(generate_team("team_red", "team_blue", "team_yellow"))
    
# function as parameter of another function
def square_numbers(n):
    return n*n
def apply_something(a, b):
    return a(b)
print(apply_something(square_numbers, 3))

    
