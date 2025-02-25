# class Fruit():

#     def __init__(self,name,calories):
#         self.name=name
#         self.calories=calories

#     def __str__(self):
#         return f"{self.name}:{self.calories}"
#     def __len__(self):
#         return self.calories

# myFruit=Fruit("banana",150)
# print(myFruit.calories)
# print(myFruit.name)
# print(myFruit)
# print(len(myFruit))

class Train():

    def __init__(self,name):
        self.name=name
    def __getitem__(self,key):
        if key==["a"]:
             return self.name
        else:
            return "not found"
    

       
    
myTrain=Train("myTrain")    
print(myTrain["a"])