class Musıcıan():

    def __init__(self,name):
        self.name=name
        print("Musıcıan class")
    def test1(self):
        print("test1")
    
    def test2(self):
        print("test2")

atıl=Musıcıan("atıl")
print(atıl.name)
print(atıl.test1())
print(atıl.test2())

class MusıcıanPlus(Musıcıan):

    def __init__(self,name):  
        Musıcıan.__init__(self,name)
        print("musıcıan plus")
    def test3():
        print("test3")
    #overrıde
    def test1(self):
        print("test1 test1 test1 , seviyom seni :D")
        

atlas=MusıcıanPlus("atlas")
print(atlas.name)
atlas.test1()
atlas.name="atlas samancıoglu"
print(atlas.name)