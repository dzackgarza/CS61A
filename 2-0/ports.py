'''
Author: Zack Garza
'''

ports = ["Oakland", "Long Beach", "Hong Kong", "Kaohsiung", "Naha", "Yokohama", "Oakland"]

name = input("Enter new port name: ")
number = int(input("Enter number of the new port in the itinerary: "))

print(str(ports))
ports[number] = name
print(str(ports))
