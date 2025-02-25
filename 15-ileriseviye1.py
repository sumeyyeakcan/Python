#range 
range(50)

# for num in list(range(20)):
#     print(num*2)

# print(list(range(20)))
# print(list(range(5,25,2)))

# my_list=[10,20,30,40]
# for num in my_list:
#     print(num)

# my_list=[10,20,30,40,50]
# for index in range(len(my_list)):
#     print(my_list[index])

#enumerate

# myList=[10,20,30,40]
# for element in enumerate(myList):
#     print(element)

# myList=[10,20,30,40,50]
# for (ix,value) in enumerate(myList):
#     print(ix)

#random
from random import randint
# print(randint(0,20))

from random import shuffle
my_list=[1,2,3,4,5,6,7,8,9,10]
shuffle(my_list)
print(my_list)

my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list[randint(0,len(my_list)-1)])

    