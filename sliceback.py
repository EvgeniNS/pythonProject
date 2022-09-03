#          01234567890123456789012345---25 -26
letters = "abcdefghijklmnopqrstuvwxyz"
# very long = = == == = = = = =V
backwards = letters[::-1] # if you will use [25:0:-1] you will get zyxwvutsrqponmlkjihgfedcb but without the A ,to get the A you need or do the reverse maximum in that example it will be -27 but much easyer just not to write enythink and python will go to the maximum value and you can use it the 2 position from [25:-27:-1] to 2[25::-1] or [:-27:-1] or [::-1]
print(backwards)

print("----")

backwardss = letters[-10:-13:-1]
print(backwardss)

print("----")

backwardsss = letters[-22::-1]    # you can put -27 in [-22:-27:-1] and get the same result
print(backwardsss)

print("----")

backwardssss = letters[:-9:-1]
print(backwardssss)