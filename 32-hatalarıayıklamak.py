#try - except
# while True:
#     try:
#         myAge=int(input("enter your age:"))
#         print(myAge*2)
#         break
#     except ValueError:
#         print("enter your age!!!")
#     else:
#         print("else executed")
#     finally:
#         print("finally")

try:
    color = input("en sevdıgın renk nedır:")
    if color.isdigit():
        print("Rakam girmeyiniz")
except:
    print(f"En sevdiğiniz renk {color}")

print(help(color.isdigit))

color = input("En sevdiğiniz renk: ")

try:
    int_color = int(color)
    print("Sayı girme amk mal mısın")
except ValueError:
    print(f"En sevdiğiniz renk {color}")

color = input("En sevdiğiniz renk: ")

try:
    int_color = int(color)
    if int_color:
        print("Sayı girme amk mal mısın")
except ValueError:
    print(f"En sevdiğiniz renk {color}")