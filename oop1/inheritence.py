# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class 
# base class, parent class
class BaseClass:
    pass

# derived class or child class
class DerivedClass(BaseClass):
    pass
"""
1. simple inheritance: parent class --> child class (Gadget ---> Phone) (Gadget --> Laptop)

2. Multi-level inheritance: Granda --> Parent --> child (Vehicle --> Bus ---> ACBus) (Vehicle --> Truck --> PickupTruck)

3. Multiple inheritance: Student (Family, School, Sports)

4. Hybrid: Granda --> Father, Uncle, Aunty --> Child (Father, Uncle)
"""
class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running laptop: {self.brand}'
    
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}'

# inheritance
my_phone = Phone('iphone', 120000, 'silver', 'china', True)
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)