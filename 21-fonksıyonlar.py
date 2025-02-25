#methods vs functıon

# def hellopython():
#     print("hello")
#     print("python")
# hellopython()
#input


# def helloPython(name):
#     print("hello")
#     print(name)
# helloPython("sümeyye")

# def sumExample(num1,num2):
#     print(num1+num2)

# sumExample(23,45)

# def hello_surname(surname="akcan"):
#     print("hello")
#     print(surname)
# hello_surname("selma")

# def summantıon(num1,num2,num3):
#     print(num1+num2+num3)
# x=summantıon(20,34,56)
# print(x)

# def return_summanatıon(num1,num2,num3):
#     result=num1+num2+num3
#     print(result)
#     return result
# x=return_summanatıon(20,30,40)
# print(x)

# def control_string(s):
#     if s[0]=="a":
#         print("a")
# control_string("aslan")

#args ,kwargs arguments key word arguments


# def args_sum(*args):
#     return sum(args)

# print(args_sum(12,23,45,56,78))

# def args_example(*args):
#     print(args)

# args_example(1,2,3,4,5)

def kwargs_example(**kwargs):
    print(kwargs)

kwargs_example(banana=100,apple=200,melon=300)

def kwargs_example2(**kwargs):
    if "apple" in kwargs:
        print("appleeeeee")
    else:
        print(":(")
kwargs_example2(apple=100,melon=300)