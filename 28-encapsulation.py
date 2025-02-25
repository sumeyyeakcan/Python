class Phone():

    def __init__(self,name,price):
        self.name=name 
        self.__price=price
    def info(self):
        print(f"{self.name} price is: {self.__price}")
    def changePrice(self,price):
        self.__price=price

ıphone=Phone("iphone",500)
ıphone.changePrice(400)


print(ıphone.info())