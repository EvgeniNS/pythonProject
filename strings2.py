#         012345678901234 0 is the first letter , if you use -1 to example you will start from the end without 0
parrot = "Norwegian Blue"

print(parrot[0:6])    # Norweg  if you doing 0:6 your not including the 6 letter
print(parrot[3:5])    # we
print(parrot[0:9])    # Norwegian  the 9 is not included but if you will use it without the : like [9] its will mean the 9 letter like in line 31 and above
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

print('----------')
#          01234567890123456789012345---25 -26   "Hi My name is evgeni and im learning strings"
letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[25])
print(letters[25:26])

print('----')

print(letters[4] + letters[21] + letters[6] + letters[4] + letters[13] + letters[8])

print('----')

print(letters[4:5] + letters[21:22] + letters[6:7] + letters[4:5] + letters[13:14] + letters[8:9])

print('----')
#-------------------------------------------------------------------its the letter 4:e from the start   -   V |\ V  -  its the amount of the letter from the end to start if it was like ,g:-20 ,f:-21 ,e:-22 ,d:-23 ,c:-24 ,b:-25 , a:-26 and its end on z:-1 not on 0
print(letters[-22] + letters[-5] + letters[-20] + letters[-22] + letters[-13] + letters[-18])    # im doing 4 - 26 = -22 and ex...

print('----')

print(letters[-22:-21] + letters[-5:-4] + letters[-20:-19] + letters[-22:-21] + letters[-13:-12] + letters[-18:-17])    #becuse im using the -26 letters its work like when [25:26] its from 25 to 26 but not including the the 26 the same works to [-22:-21] its from -22 to -21 but not including -21.

print('----')

#      012345678901234567890123456==26 -27   "Hi My name is evgeni and im learning strings"
kek = " abcdefghijklmnopqrstuvwxyz"

print(kek[8] + kek[9] + kek[0] + kek[13] + kek[-2] + kek[0] + kek[14] + kek[1] + kek[13] + kek[5] + kek[0] + kek[9] + kek[-8] + kek[0] + kek[5] + kek[22] + kek[7] + kek[5] + kek[14] + kek[9] +
      kek[0] + kek[1] + kek[14] + kek[4] + kek[0] + kek[9] + kek[13] + kek[0] + kek[12] + kek[5] + kek[1] + kek[-9] + kek[14] + kek[9] + kek[14] + kek[7] + kek[0] + kek[-8] + kek[-7] + kek[-9] + kek[9] + kek[14] + kek[7] + kek[-8])
