count=0
# while count <=5:
#     print(count)
#     count=count+1

# Infinite loop
# while True:
#     print(count)
#     count=count

# Loop with else statement
# while count<5:
#     print (count)
#     count=count+1
# else:
#     print ("Statement ends here")

# while count<5:
#     print (count)
#     count=count+1
#     if count==2:
#         break

# while count<5:
#     if count==2:
#         count=count+1
#         continue

#     print (count)
#     count=count+1

# for loop
# syntax
# for iterator in elements:
# no=[1, 2, 3, 4, 5]
# for n in no:
#     print (n)

# course="python"
# for c in course:
#     print(c)

# create a dictionary
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

# for p in person:
#     print(p)
# for key, values in person.items():
#     print(values)

# create set of companies and loop 
# Companies={"Google", "Amazon", "Microsoft", "Facebook"}
# for comp in Companies:
#     print(comp)

# using break and continue in the "for in" loop
# break
Nos=(7, 9, 2, 5, 12, 4, 7)
# for N in Nos:
#     print(N)
#     if N==3:
#         break

# continue
# for N in Nos:
#     print(N)
#     if N==3:
#         continue
#     print("next number should be", N+1) if N !=7 else print("loop ends")

# range
# lst=list(range(7))
# print(lst)

# st=set(range(1,7))
# print(st)

# lst=list(range(0,11,2))
# print(lst)

st=set(range(1,10,2))
print(st)

# nested loop 
# for a in b:
#     for c in a:
#         print(c)

for keys in person:
    if keys=="Skills":
        for values in person["Skills"]:
            print(values)
        else:
            print("loop ends here")