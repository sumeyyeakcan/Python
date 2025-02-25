# x=5
# y=3
# z=6
# print(x>y and z<x)
# print(x<y and z>y)

# my_dictionary={"k1":"a","k2":"b","k3":"c"}
# for (key,value) in my_dictionary.items():
#     if value=="c":
#         print("c gecmektedır")
#         break

# my_other_dictionary={"a":"b","b":"c","c":"d"}
# for (key,value) in my_other_dictionary.items():
#     if key=="a":
#         print("a gecmektedır")
#         break

# my_numbers=[1,2,3,4,5,6,7,8,9,10,12,13,24,45,65]
# for i in my_numbers:
#     if i%2==0:
#         print(i)


# r_list=[2,3,45,6,12,47]
# c_list=[]
# for i in r_list:
#     c_list.append(i*2*3.14)
# print(c_list)




# from turtle import *

# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# end_fill()
# done()


# age_name_list=[("ahmet",30),("mehmet",40),("ceyda",50)]
# yas_listesi=[]
# for (isim,yas) in age_name_list:
#     yas_listesi.append(yas)
# print(yas_listesi)

# from random import randint
# metal_list=["metallıca","dc","dream theeater","megadev"]
# print(metal_list[randint(0,len(metal_list)-1)])


number_list=[5,17,84,101,462]    
new_list=[num%2==0 for num in number_list]
print(new_list)


    