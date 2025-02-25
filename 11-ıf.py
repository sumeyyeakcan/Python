# my_hero="Batman"
# print(my_hero=="Batman")
# print(my_hero!="superman")

# my_super_hero="Batman"

# if my_super_hero=="Batman":
#     #indentation
#     print("sümoş")
#     print("eyv")

# if 3>2:
#     print("atıl samancıoglu")
#     print("sümeyye akcan")

# my_super_hero=input("super kahraman ısmı gırınız:")
# if my_super_hero=="batman":
#     print("batman canım")
# elif my_super_hero=="aquaman":
#     print("su bacım")
# elif my_super_hero=="spiderman":
#     print("pis örümcek")
# else:
#     print(":(")

# my_age=23
# if my_age<=18:
#     print("age<=18")
# elif my_age>18 and my_age<=30:
#     print("18-age-30")
# elif my_age>30 and my_age<=40:
#     print("30 -age- 40")
# else:
#     print("age>40")

my_super_hero=input("super kahraman giriniz:")
my_super_hero_list=["superman","wonder woman","aquaman","spiderman"]
if my_super_hero in my_super_hero_list:
    print(":)")
else:
    print(":(")