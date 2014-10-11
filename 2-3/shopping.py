shoppingList = []

items = int(input("How many items would you like to add? "))

for i in range(0, items):
	shoppingList.append(input("Enter item " + str(i+1) + ": "))

print("Your list: ")
for item in shoppingList:
	print(item)
