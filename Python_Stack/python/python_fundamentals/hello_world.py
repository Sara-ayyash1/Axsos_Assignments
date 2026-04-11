# 1. TASK: print "Hello World"
print(  "Hello World" )

# 2. print "Hello Noelle!" with the name in a variable
name = "Sara"
print( "Hello" , name )    # with a comma
print( "Hello " + name )    # with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello" , name )    # with a comma
#print( "Hello" + name )    # with a +    -- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}".format(fave_food1 , fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}" ) # with an f string

#-------------------------------------------------------------------------

my_string = "hello Sara, welcome to AxsoS academy 2026"
words_list = ["Python", "is", "fun"]

# 1. string.upper(): Converts all characters in the string to uppercase.
print(my_string.upper()) 

# 2. string.lower(): Converts all characters in the string to lowercase.
print(my_string.lower()) 

# 3. string.count(substring): Returns the number of times a value appears in the string.
print(my_string.count("a")) 

# 4. string.split(char): Splits the string into a list based on a specific character.
print(my_string.split(" ")) 

# 5. string.find(substring): Returns the index (position) of the first occurrence of a value.
print(my_string.find("Sara")) 

# 6. string.isalnum(): Returns True if all characters in the string are alphanumeric.
print(my_string.isalnum()) 

# 7. string.join(list): Joins the elements of a list into one string using a separator.
print("-".join(words_list)) 

# 8. string.endswith(substring): Returns True if the string ends with the specified value.
print(my_string.endswith("2026"))