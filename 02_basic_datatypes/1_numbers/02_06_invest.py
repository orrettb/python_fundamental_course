'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
#get inputs for user
investment_amount = float(input("How much do you have to invest?:"))
interest_rate = float(input("What's your desired interest rate in decimals?:"))
years_to_invest = int(input("How many years do you have to invest?:"))
#calculate future values
future_values = investment_amount * ((1 + interest_rate) ** years_to_invest)
#print to console
print("Your future value of your investment is {}.".format(future_values))