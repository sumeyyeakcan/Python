class Person():
    #property
    #name=""
    #age=0
    #gender=""
    job="developer"

    #method,initializer
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printName(self):
        print(self.name)
    

# myList=list()
# type(myList)

# atıl=Person()
# print(type(atıl))
# atıl.age=35
# atıl.name="sümeyye akcan"
# print(atıl.age)

# atıl=Person()
# atlas=Person()
# type(atıl)
# type(atlas)

atıl=Person("atıl",35,"male")
print(atıl.age)
print(atıl.printName)
print(atıl.job)