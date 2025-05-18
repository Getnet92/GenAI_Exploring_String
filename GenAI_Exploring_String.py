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

# Task 3
palindrome = str(input("Enter your palindrome: ")) # prompting user to enter palindrome
palindrome = palindrome.strip() # stripping white space if appears
size = int(len(palindrome)) # taking the size of the string to use for the number of iterations needed
check = palindrome[::-1]
n = 0 # to be later used to compare against the size of the string 
for i in range (size):
    if ( palindrome[i] == check[i]): # condition to update n to later display message depending on value of n
        n+=1
    else:
        print("This word is not a palindrome")
        break # breaking if conditions aren't met to stop checking, only 1 letter is needed to be misplaced

if n == size: # only runs if n is equal to size meanding the number of letters in the correct order equal the size of the string meaning the word and it's reverse are the same word
    print(palindrome + " is a palindrome ")
