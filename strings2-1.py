#         012345678901234 0 is the first letter , if you use -1 to example you will start from the end without 0
parrot = "Norwegian Blue"
#                V = its mean the amount of steps that it will jump now its 2 for example in this word Pidoras = Pdrs and if the jump will be 3 its will be Pidoras = Pos
print(parrot[0:6:2])   #Nre
print(parrot[0:6:3])   #Nw

number = "9,223;372:036 854,775;807"
print(number[1::4])
seperators = number[1::4]
print(seperators)
# on the first attempt i forgot to space here ========V  and it work differnt so its very importent
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])