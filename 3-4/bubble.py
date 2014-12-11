def bubble_sort(items):
    inOrder = False
    while(not inOrder):
        inOrder = True
        n = 0
        while n < len(items) - 1:
            if items[n] > items[n + 1]:
                inOrder = False
                items[n], items[n + 1] = items[n + 1], items[n]
            n += 1
    return names

names = ["C++", "Java", "Python", "C#", "COBOL", "FORTRAN"]

print(names)
names = bubble_sort(names)
print(names)
