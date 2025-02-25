# def divideNumber(num):
#     return num/2

# print(divideNumber(20))

# my_list=[10,20,30,40,50,60,70]
# my_result_list=[]
# for i in my_list:
#     my_result_list.append(divideNumber(i))
# print(my_result_list)

# my_list=[10,20,30,40,50,60,70]
# my_result=list(map(divideNumber,my_list))
# print(my_result)

# def controlString(string):
#     return "atıl" in string

# print(controlString("atıl samancıoglu"))

# my_string_list=["esma","ahmet","cem","atıl"]
# print(list(map(controlString,my_string_list)))

# my_string_list=["esma","ahmet","cem","atıl"]
# print(list(filter(controlString,my_string_list)))

#lambda
my_result=lambda num:num*3
print(my_result(2))

num_list=[10,20,30,40,50]
print(list(map(lambda num:num/4,num_list)))

