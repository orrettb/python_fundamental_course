'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
#take 3 inputs from user
input_1 = input("Enter a word:")
input_2 = input("Enter a second word:")
input_3 = input("Enter a third word:")
#calcualte their lenght
len_input_1 = len(input_1)
len_input_2 = len(input_2)
len_input_3 = len(input_3)

#print result
print(len_input_1, input_1)
print(len_input_2, input_2)
print(len_input_3, input_3)