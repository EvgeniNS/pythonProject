#----V = the i is just a variuble like x in math you can change it to any letter
#----v---|\----V===V = this is the range that the reesult will be for example 1-13 it will be 12 lines of result and you cant write a number bigger then 12 for example
for i in range(1, 13): #this * 2 mean range in {2} * 2 = 4 <<<= V   |\   V>>> this ** 3 mean that the result will increase on him self like range {2} * 2 * 2 = 8
    print("No. {0} squared is {1} and cubed is {2}".format(i, i * 2 , i ** 3 ))

print("----")

for i in range(1, 13): #-----------V = if you will change this number or the : to somethink else it will chnage the anount of space that the numbers will have in the result
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print("----")

for i in range(1, 13):  #-----------V = if you will add < the result will go from 3 number to 1
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("----")

for i in range(1, 13):  #------------------------------V = if you will add ^ it will center the result
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print("----")

print("Pi is approximately {0:12}".format(22 / 7)) # the defult amount of nambers in the result is 12
print("Pi is approximately {0:12f}".format(22 / 7)) # the F in the {0:12f} is to change the defult amount of numbers that will be in the result F = 6
print("Pi is approximately {0:12.50f}".format(22 / 7)) # in this example the {0:12.50f} you have 50f that mean 50 points after the decimal point
print("Pi is approximately {0:52.50f}".format(22 / 7)) # in this example the {0:52.50f} the 52 is the width of space that the result will have
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:72.54f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print("----")

for i in range(1, 13):  #----------------------V = the width of space
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))


