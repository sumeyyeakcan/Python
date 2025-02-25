# def toplama(a,b):
#     print(a,b)

# x=toplama(3,4)
# print(x)

# def usselIslem(num1=5,num2=3):
#     print(num1**num2)

# print(usselIslem(2,4))
# print(usselIslem())

# def myLoop(*args):
#     for element in args:
#         print(element/2)
# print(myLoop(3,2,1,5,3,4))

# def myFunction(num):
#     return num**3
# myList=[2,3,4,5,6]
# for i in myList:
#     print(myFunction(i))
# print(list(map(myFunction,myList)))

# barkodDizisi=["abc1221324","xyz35465","abc123"]
# def controlString(string):
#     return "xyz" in string
# print(list(filter(controlString,barkodDizisi)))
    
myVar="atıl samancıoglu"
def ornekFonksıyon():
    myVar="atıl"

    def dıgerFonksıyon():
        print(myVar)
    dıgerFonksıyon()
print(ornekFonksıyon())

# class Kedi():

#     def __init__(self,isim,yas=5):
#         self.isim=isim
#         self.yas=yas
#     def yasıCarp(self):
#         return self.yas*3
# kedim=Kedi("tonton")
# print(kedim.yasıCarp())
    
class Ogrencı():

    def __init__(self,isim,sınavNotu):
        self.isim=isim
        self.__sınavNotu=sınavNotu
    def notuGoster(self):
        print(f"{self.isim} sınav notu {self.__sınavNotu}")

öğrenci=Ogrencı("mehmet",85)
öğrenci.__sınavNotu=75
print(öğrenci.notuGoster())

#abstractıon