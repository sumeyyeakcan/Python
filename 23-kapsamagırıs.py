# x=20

# def multıply(num):
#     x=5
#     return num*x
# print(multıply(5))

#LEGB local,enclosıng,global,buılt-ın
#global
# myString="atıl"

# def myFunction():
#     #enclosıng
#     myString="atıl 2"

#     def myFunction2():
#         #local
#         myString="atıl 3"
#         print(myString)

# print(myString)
# print(myFunction)

# def test1():
#     myVariable=10
#     print(myVariable*2)

# def test2():
#     print(myVariable*3)


# y=10

# def newFunction(y):
#     print(y)
#     y=5
#     print(y)
#     return y

# print(newFunction(10))

y=10

def change():
    global y
    y=5
    print(y)
print(change())
print(y)
