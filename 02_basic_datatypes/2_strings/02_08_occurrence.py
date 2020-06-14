'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
#take input of string
user_words = input("Enter a sentence of your choosing:")
#take input of a letter
letter = input("Enter one letter from the english alphabet:")
#find index of first occurence of that letter
result = user_words.find(letter)
#print result
print(result)