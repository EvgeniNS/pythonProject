print("Today is a good day to learn python")
print('Python is fun')
print("Python's strings are easy to use")
print('we can even include "quatos" in strings')
print("hello" + "world")
greeting = "Hello"
name = input("Please enter your name ")
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))
#VVV i added A to age that i can check the error on line 23-25
aage = "2 years"
print(aage)
print(type(aage))

age_in_words = "2 Years"
print(name + " is " + "age" + " years old") # if you will just put age without the "" its will give you n error
print(type(age))

e_in_words = "2 Years"
print(name + f" is {age} years old") # if you will add f to start of the "" it will give you an option to add
print(type(age))