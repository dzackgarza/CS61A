import math

def puzzle1(s1, s2):
	e1, e2 = s2[0:math.ceil(len(s2)/2)] , s2[math.ceil(len(s2)/2):len(s2)]
	return e1.upper() + s1.lower() + e2.upper()

def reverse(s):
	return "".join(reversed(s))

def double(s):
	return s + s

def unfinished(s):
	return s[0:len(s)-2] + ".."

print("1: " + puzzle1("Exercise", "Class"))
print("2: " + puzzle1("SQL", "Python"))
print("3: " + reverse("Engineering"))
print("4: " + double("Trouble"))
print("5: " + unfinished("Business"))
