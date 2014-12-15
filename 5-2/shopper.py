class Shopper:
    items = []
    
    def __init__(self, items = []):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def print_items(self):
        for i in self.items:
            print i

class Item:
    price = ""
    quantity = 0
    size = ""

    def __init__(self, price, quantity = 1, size = ""):
        self.price = price
        self.quantity = quantity
        self.size = size
    
    def change_price(self, price):
        self.price = price

    def add_one(self):
        self.quantity += 1

    def subtract_one(self):
        self.quantity -= 1
        if self.quantity < 0:
            self.quantity = 0

    def __str__(self):
        return str(self.price) + "," +  str(self.quantity) + "," +  str(self.size)
