class CokeMachine():

    """
    Simulates the internal workings of a coke machine.
    """

    balance = 1000  # 10 dollars, 1000 cents for integer arithmetic.
    nickels = 20
    dimes = 10
    quarters = 4 * 8

    inserted_coins = 0
    accepted_coin_values = [5, 10, 25, 100, 500]

    # Name, [Number left in stock, Price]
    inventory = {
        "Coke": [10, 100],
        "Sprite": [10, 100],
        "Dr. Pepper": [10, 100],
        "Diet Coke": [10, 100],
        "Coke Zero": [10, 100],
        "Vanilla Coke": [10, 100]
    }

    def __init__(self):
        self.init_balance()

    """
    Populate this machine's change registers with 10 dollars in various coins.
    """

    def init_balance(self):
        self.balance = 1000
        self.nickels = 20
        self.dimes = 10
        self.quarters = 4 * 8
        assert self.sum_change() == self.balance

    """
    Returns the amount of money (in cents) in this machine.
    """

    def sum_change(self):
        sum = self.quarters * 25
        sum += self.dimes * 10
        sum += self.nickels * 5
        return sum

    """
    Give the name of a type of soda, dispenses it if enough change has been
    inserted and there is still at least one in stock. Then returns True.
    If not enough money inserted or no stock left, returns False.
    Prints corresponding status messages.
    """

    def make_purchase(self, selection):
        if selection not in self.inventory.keys():
            print("Selection does not exist, please try another.")
            return False
        elif self.inventory[selection][0] == 0:
            print("Currently out of that selection, please try another.")
            return False
        elif self.inserted_coins >= self.inventory[selection][1]:
            print("Dispensing " + str(selection) + "!")
            self.inventory[selection][0] -= 1
            self.inserted_coins -= self.inventory[selection][1]
            if self.inserted_coins > 0:
                self.return_coin(self.inserted_coins)
                self.inserted_coins = 0
            return True
        else:
            print("Not enough coins inserted. Please insert " +
                  self.int_to_dollars(
                      self.inventory[selection][1] - self.inserted_coins)
                  + " more.")

    """
    Given a value in cents, accepts the coin and adds it to the running
    total money inserted and returns True. If the value given does not
    correspond to some known coin value, returns False.
    """

    def insert_coin(self, value):
        if value in self.accepted_coin_values:
            self.inserted_coins += value
            print("Added " + self.int_to_dollars(value))
            print("Total Inserted: "
                  + str(self.int_to_dollars(self.inserted_coins)))
            return True
        else:
            print("Sorry, your coin was not accepted.")
            self.return_coin(value)
            return False

    """
    Prints an error message and returns the last coin.
    (Intended to pass a message to the coin-return mechanism)
    """

    def return_coin(self, value):
        print("Returning coins equal to "
              + str(self.int_to_dollars(value)))

    """
    Basic string formatting for the LED display.
    """

    def int_to_dollars(self, value):
        if value > 100:
            return str(value / 100) + " dollars"
        else:
            return str(value) + " cents"

    """
    Pass in a type of soda and a quantity to update the internal
    inventory count.
    """

    def stock_up(self, selection, quantity):
        self.inventory[selection][0] += quantity

    def addSoda(soda, quanitity):
        pass


class Soda:

    name = "Coke"
    price = 100

    def __init__(self, button, name="Coke", price=100, buttonID=0):
        self.name = name
        self.price = price
        self.buttonID = buttonID
        self.button = button


class Button:

    name = "Default"
    id = 0

    def __init__(self, name, soda, function):
        self.name = name
        self.soda = soda
        self.function = function


m = CokeMachine()

m.make_purchase("Coke")
m.insert_coin(25)
m.make_purchase("Coke")
m.insert_coin(25)
m.make_purchase("Coke")
m.insert_coin(25)
m.make_purchase("Coke")
m.insert_coin(25)

# Should have enough now
m.make_purchase("Coke")

# Should reject pennies
m.insert_coin(1)

m.insert_coin(500)
m.insert_coin(100)
m.make_purchase("Diet Coke")
# Should return 5 dollars

# Should run out after dispensing ten
for i in range(0, 11):
    m.insert_coin(100)
    m.make_purchase("Sprite")
