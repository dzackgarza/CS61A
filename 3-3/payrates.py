rates = [
    # <2   >2    >3    >4   >5
    [1516, 1516, 1516, 1516, 1516],  # E-1
    [1700, 1700, 1700, 1700, 1700],  # E-2
    [1787, 1900, 2015, 2015, 2015],  # E-3
    [1980, 2081, 2194, 2305, 2403],  # E-4
    [2159, 2304, 2416, 2530, 2707],  # E-5
    [2357, 2594, 2708, 2819, 2935],  # E-6
    [2725, 2974, 3088, 3239, 3357],  # E-7
]


def get_rate(grade, years):
    if years >= 6:
        col = 4
    elif years >= 4:
        col = 3
    elif years >= 3:
        col = 2
    elif years >= 2:
        col = 1
    else:
        col = 0

    return rates[grade - 1][col]

grade = int(input("Enter pay grade as an integer: "))
yos = float(input("Enter years of service: "))
print(str(get_rate(grade, yos)))
