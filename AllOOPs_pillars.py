from abc import ABC ,abstractmethod
class Vehicle(ABC):
    def __init__(self,brand,color,model):
        self.__brand=brand
        self.color=color
        self.model=model
    @abstractmethod
    def start(self):
        pass
    def get_brand(self):
        return self.__brand
class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color, model) 
    def start(self):
        print("CAR is started")
        print("carbrand of the car: ",self.get_brand())
        print("colorof the car: ",self.color)
        print("modelof the car: ",self.model)
class Bike(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color, model)
        
    def start(self):
        print("Bikebrand: ",self.get_brand())
        print("color: ",self.color)
        print("model: ",self.model)
        print("BIKE is started")
c=Car("KIA","white",2021)
c.start()
b=Bike("TVS","black",2024)
b.start()
    
    