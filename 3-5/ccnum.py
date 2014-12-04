name = input("Enter 16 digit credit card number: ")
stripped = name.replace(" ", "")
if len(stripped) != 16:
    print("Input was not 16 digits.")
elif not stripped.isdigit():
    print("String contained a non-numeric character.")
else:
    print("String verified.")
    print("Database string: ", stripped)
