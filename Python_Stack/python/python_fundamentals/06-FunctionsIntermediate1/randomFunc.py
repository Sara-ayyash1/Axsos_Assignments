import random

def randInt(min=  0 , max= 100  ):
    if min > max:
        min, max = max, min

    num = random.random() * (max - min ) + min
    return round(num)

print(randInt())             # should print a random integer between 0 to 100
print(randInt(max=50))         # should print a random integer between 0 to 50
print(randInt(min=50))         # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

#BONUS: account for any edge cases (eg. min > max, max < 0)
print(randInt(min=50, max=10)) #min > max => swap
print(randInt(min=-100, max=-50)) # max < 0 and max > min its the normal case
print(randInt(min=-40, max=-50)) # max < 0 and min > max => swap
print(randInt(min=50, max=50)) # it always give us 50



#To Remeber
# random.random() returns a random floating number between 0.000 and 1.000

#if we have a max => random.random() * 50
# random.random() * 50 returns a random floating number between 0.000 and 50.000

#if we  have a max and min => random.random() * (max - min) + min
# random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000

# round(num) returns the rounded integer value of num