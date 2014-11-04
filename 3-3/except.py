name = "Zack"
print("Name: " + name)
try:
    print("Attempting to square the name.")
    square = name ** 2
except TypeError:
    print("Sorry, name can not be squared.")
