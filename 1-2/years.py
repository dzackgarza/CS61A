"""
Calculating the number of seconds in a given amount of years.

Laney College, 2014
Zack Garza
"""

def calcYear():
	years = int(input("Tell me a number of years! "))

	secondsPerMin = 60
	minsPerHour = 60
	hoursPerDay = 24
	daysPerYear = 365

	print("That's " + str(years * daysPerYear * hoursPerDay * minsPerHour * secondsPerMin) + " seconds!")

calcYear()
