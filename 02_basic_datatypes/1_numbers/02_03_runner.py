'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
#convert miles to kilometers
kilo_meters = 10 * 1.6
#convert time to hours
hrs = ((30 * 60) + 30) / 3600
#calculate average speed
average_speed = kilo_meters / hrs
#print result
print(average_speed)