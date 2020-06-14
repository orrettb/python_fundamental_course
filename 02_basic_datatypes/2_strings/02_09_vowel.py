'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
#get string from user
user_words = input("Enter a sentence:")
#count the vowels
count = 0
for char in user_words:

    vowels = "aeiouAEIOU"
    if char in vowels:
        count += 1

#print total
print(count)
