'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
#take the users name via input
user_name = input("Enter your first name:")
#select the first letter
fist_letter = user_name[0]
#add pig latin variable
pig_value = "ay"
pig_latin_ver = user_name[1:]+fist_letter+pig_value
#print result
print(pig_latin_ver)