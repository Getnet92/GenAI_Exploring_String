# Task 1
s = "Python is amazing!"
# first 6 characters
first_six= s[0:7] 
print("The first 6 characters are: " + first_six)
# amazing
amazing = s[10:18]
print("The last word is: " + amazing)
# reverse
reverse_string = s[::-1] 
print("The phrase in reverse is: " + reverse_string)

# Task 2
word = " hello, python world! "

#using 
strip_word = word.strip() # using the strip function
print("The word stripped looks like: " + strip_word)
# First letter capitalized
capital_first = (" " + strip_word.capitalize() + " ") # white space before and after the stripped word to keep the white space
print("The first letter capitalized: " + capital_first)
# replacing world with universe
replica_word = (word.replace("world" , "universe")) # using the replace funcution
print(replica_word)