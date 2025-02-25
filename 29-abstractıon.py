from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def maxSpeed(self):
        pass


class Tesla(Car):

    def maxSpeed(self):
        print("200 km")
    

tesla=Tesla()
print(tesla.maxSpeed())


class Mercedes(Car):

    def maxSpeed(self):
        print("300 km")

mercedes=Mercedes()
print(mercedes.maxSpeed())