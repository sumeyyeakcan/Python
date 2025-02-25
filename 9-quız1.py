my_string = "James Hetfield"
my_letter=my_string[5]
print(my_letter)

my_new_string = "QuentinTarantino"
print(my_new_string[5:8:])

my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"
print(my_last_string[::-1])

print(3+10.2+50)
print(5 + 8 * 12)

my_list=[1,2,"a"]
my_list.append(1)
my_list.append(2)
my_list.append("a")
print(my_list)
myList=list(my_list)
print(myList)

my_list = [1,4,[2,3,"a"]]
print(my_list[2][2])

my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]}
print(my_dictionary["kk"][1]["kkkk"])

my_list_to_be_set = [11,12,22,33,11,22,45,32,21,22,33,45]
my_set=set(my_list_to_be_set)
print(my_set)

x = 40 * 5 + 3
y = 208 - 2 * 4
print(x > y)

a = 40 * (4 - 2)
b = 80 - 2 * -5
print(a > b)
