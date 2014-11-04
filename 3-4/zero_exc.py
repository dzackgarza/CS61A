def div(p, q):
    if q == 0:
        raise ZeroDivisionError("Denominator can not be zero.")
    else:
        return p / q

print("Divide two numbers.")
p = float(input("Enter numerator: "))
q = float(input("Enter denominator: "))

print(str(div(p, q)))
