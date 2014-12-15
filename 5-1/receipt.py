class Receipt:
    from = ""
    to = ""
    address = ""
    packages = []
    receivedBy = ""
    CODCharge = 0.00

    def __init__(self):
        pass

    def addPackage(self, package):
        self.packages.append(Package)

    def totalWeight(self):
        total = 0
        for p in self.packages:
            total += p.getWeight()
        return total

    def totalPackages(self):
        total = 0
        for p in self.packages:
            total += p.numPackages
        return total

    def deliveryCharge(self):
        pricePerOz = 2.00
        total = 0
        for p in self.packages:
            total += p.getWeight() * pricePerOz
        return total

class Package:
    numPackages = 1
    description = ""
    weight = "1 oz."

    def __init__(self, number = 1, description = ""):
        pass

    def getWeight(self):
        pass

    def describe(self, message):
        self.description = message
