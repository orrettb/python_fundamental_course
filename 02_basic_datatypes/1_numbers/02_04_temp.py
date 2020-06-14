'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
#get fahrenheit from user
f = float(input("Enter Fahrenheit temperature:"))
#calculate celsius
c = (f - 32) * (5 / 9)
#print output
print("{} degrees fahrenheit = {} degrees celsius".format(f, c))