"""
Calculates a current balance for annually compounded interest in an account.

Laney College, 2014

@date		9/22/2014
@author 	Zack Garza <dzackgarza@gmail.com>
"""

principal = int(input("What is the principal amount in dollars? "))
rate = int(input("What is the annual interest rate as a percentage? ")) 
years = int(input("What is the term, in years? "))

step1 = rate/100
step2 = 1 + step1
step3 = pow(step2, years)
balance = principal * step3

print("Your balance is: $" + "%.2f" %  balance)
print("Balance: " + format(%.2f)
