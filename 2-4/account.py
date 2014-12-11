"""
Based on the Account class, considering special tax implications for 401k
"""
class Account401k:

	holder = "" 				# Name of the account holder
	interest = 0.00 		# Baseline interest rate
	balance = 0.00 			# Current account balance (in dollars)
	timeSinceBirth 			# Number of seconds since birth

	# Create a new account - send in the birthday, it's transformed into seconds
	def __init__(self, interest=0.00, holder="", amount=0.00, birthdate = ""):
		self.interest = interest
		self.holder = holder
		self.amount = amount
		self.timeSinceBirth = self.getTimeSinceBirth(birthdate);

	# Transforms a birthdate string into a number of seconds
	def getTimeSinceBirth(birthdate): pass;

	# Add money to account
	def deposit(self, amount):
		self.balance += amount
		return self.balance

	# Handles logic for all withdrawals
	def withdraw(self, amount):

		secondsPerYear = 60 * 60 * 24 * 365;
		taxPenaltyAge = secondsPerYear * 59.5;
		mandatoryWithdrawalAge = secondsPerYear * 70.5;

		mandatoryWithdrawalAmount = 100;
		if (self.timeSinceBirth > mandatoryWithdrawalAge):
			amount += mandatoryWithdrawalAmount;

		if (self.timeSinceBirth < taxPenaltyAge):
			return self.getEarlyWithdrawal(self, amount);
		else:
			if (self.balance < amount):
				print("Not enough funds.")
			else:
				self.balance -= amount
			return selfbalance

	# Apply tax penalties
	def getEarlyWithdrawal(self, amount): pass;

	# Query current balance
	def getBalance(self):
		return self.balance
