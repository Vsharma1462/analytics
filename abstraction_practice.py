from abc import ABC,abstractmethod

class vehicle(ABC):
    def __init__(self,n):
        self.num_of_tyre = n

    @abstractmethod
    def start(self):
        pass   
    
    def display(self):
        print("calling from vehicle")


class bike(vehicle):
    def __init__(self):
        self.num_of_tyre = 2

    def start(self):
        print("start by kick")
        
class scooty(vehicle):
    def __init__(self):
        self.num_of_tyre = 2

    def start(self):
        print("start by self start")   

class car(vehicle):
    def __init__(self):
        self.num_of_tyre = 4

    def start(self):
        print("start by key")

vehicles = [ bike(),scooty(),car() ]     
for vehicle in vehicles:
    vehicle.start()
    vehicle.display()