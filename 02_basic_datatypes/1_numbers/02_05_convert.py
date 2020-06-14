'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
x = 8
y = 7.5

#convert int to float
x = float(x)

#convert float to int
y = int(y)

#floor division with float and an int
f = float(input("Enter a float number:"))
i = int(input("Enter an interger"))
f_d = f//i

print(f_d)