#         012345678901234 0 is the first letter , if you use -1 to example you will start from the end without 0
parrot = "Norwegian Blue"

print(parrot[0:6])    # Norweg  if you doing 0:6 your not including the 6 letter
print(parrot[3:5])    # we
print(parrot[0:9])    # Norwegian  the 9 is not included
print(parrot[:9])    # Norwegian becuse we not include the x in x:9 and we just had empty space its automaticly atarts with 0

print('----')

print(parrot[10:14])
print(parrot[10:])    # if we not giveing value or X in 10:x it will go to the end

print('----')

print(parrot[:6])    # if your not including the start value X in [X:6] it will start form the start 0
print(parrot[6:])    # if your not including the end value X in [6:X] it will go the end

print('----')

print(parrot[:6] + parrot[6:])

print('----')

print(parrot[ : ])