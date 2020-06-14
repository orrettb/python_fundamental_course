'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
#take a string from user
my_str = input("Enter a sentence:")
str_lower = my_str.lower()
#take a symbol from the user
my_symbol = input("Enter a symbol")
#select the first letter
first_letter = str_lower[0]
#replace same letters with symbol
changed_str = my_str.replace(first_letter, my_symbol)
#print results
print(changed_str)