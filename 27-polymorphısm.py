class Banana():
    
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"100 calorıes {self.name}"

class Apple():

    def __init__(self,name):
        self.name=name
    def info(self):
        return f"150 calorıes {self.name}"
    
banana=Banana("banana")
apple=Apple("apple")
print(banana.name)
print(apple.name)

FruıtLıst=[banana,apple]
for fruit in FruıtLıst:
    print(fruit.info())