from abc import ABC, abstractmethod #abc = Abstract base class
from datetime import datetime

class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'

class User(ABC):
    def __init__(self,name,email,nID) -> None:
        self.name = name
        self.email = email
        #kaaj ase
        self.__id = 0 #private instance
        self.__nID = nID
        self.wallet = 0
    
    @abstractmethod
    def displayProfile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nID, currentLocation, initialAmount) -> None:
        self.currentRide = None
        self.wallet = initialAmount
        self.currentLocation = currentLocation
        super().__init__(name, email, nID)

    def loadCash(self,amount):
        if amount>0:
            self.wallet += amount

    def displayProfile(self):
        print(f"Name: {self.name} Email: {self.email}")

    def updateLocation(self, currentLocation):
        self.currentLocation = currentLocation

    def rideRequest(self, rideSharing, dest):
        if not self.currentRide:
            rideRequest = RideReq(self,dest)
            catchRide = RideMatching(rideSharing.drivers)
            self.currentRide = catchRide.findDriver(rideRequest)

    def showCurrentRide(self):
        print(self.currentRide)


class Driver(User):
    def __init__(self, name, email, nID, currentLocation) -> None:
        self.currentLocation = currentLocation
        self.wallet = 0
        super().__init__(name, email, nID)

    def displayProfile(self):
        print(f"D Name: {self.name} D Email: {self.email}")

    def updateLocation(self, currentLocation):
        self.currentLocation = currentLocation

    def acceptReq(self,ride):
        ride.setDriver(self)

class Ride:
    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
        self.driver = None
        self.rider = None
        self.startTime = None
        self.endTime = None
        self.vara = None

    def setDriver(self,driver):
        self.driver = driver

    def startRide(self):
        self.startTime = datetime.now()#Go to line 2 implement date/time

    def endRide(self,taka):
        self.endRide = datetime.now()
        self.rider.wallet -= self.vara
        self.driver.wallet += self.vara

    def __repr__(self) -> str:
        return f"Details -> Start: {self.start}|End: {self.end}"

class RideReq:
    def __init__(self,rider,endLocation) -> None:
        self.rider = rider
        self.endLocation = endLocation

class RideMatching:
    def __init__(self, drivers) -> None:
        self.fakaDriver = drivers

    def findDriver(self,rideReq):
        if len(self.fakaDriver) > 0:
            #kaaj ase
            driver = self.fakaDriver[0]
            
            ride = Ride(rideReq.rider.currentLocation, rideReq.endLocation)
            
            driver.acceptReq(ride)
            print('Kire')
            return ride
        
            

class Vehicle(ABC):
    speed = {
        'car': 50,
        'bike': 60,
        'cng': 15
    }

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'
    
    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'unavailable'



#UGES
niye_jao = Ride_Sharing('Niye Jao')
sakib = Rider("sakib Khan", 'sakib@khan.com', 1254, 'mohakhali', 1200)
niye_jao.add_rider(sakib)
kala_pakhi = Driver('Kala Pakhi', 'kala@sada.com', 5648, 'gulshan 1')
niye_jao.add_driver(kala_pakhi)
print(niye_jao)
sakib.rideRequest(niye_jao, 'uttara')
sakib.showCurrentRide()