'''A design for a motor vehicle (car, truck, motorcycle, bicycle) inheritance '''

class Vehicle: pass

class OneWheeled(Vehicle): pass
class Unicycle(OneWheeled): pass


class TwoWheeled(Vehicle): pass
class Bicycle(TwoWheeled): pass
class Motorcycle(TwoWheeled): pass
class Scooter(TwoWheeled): pass

class ThreeWheeled(Vehicle): pass
class Tricycle(ThreeWheeled): pass


class FourWheeled(Vehicle): pass
class Car(FourWheeled): pass
class Truck(FourWheeled): pass
class Van(FourWheeled): pass
class SUV(FourWheeled): pass

class ManyWheeled(Vehicle): pass
class SemiTruck(ManyWheeled): pass
