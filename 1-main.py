
name="sümoş"
print(type(name))

print(name.upper())
print(name.count("ü"))
print(len(name))
#\n --> new lıne demek 
#\t tab demek

print("sümeyye \n akcan")
print("sümeyye \t akcan")

print(name[1])
print(len(name))
print(name[len(name)-1])
print(name[-1])
print(name[-2])

barcode="ABCDEFGH123456789"
print(barcode[1])
name="sümeyye"
surname="akcan"
print(name +" " +surname)
print(100*"a")

print(name*3)

print(barcode[0]+barcode[1]+barcode[2])

#barcode[startıng ındex:stoppıng ındex:steppıng ındex]

print(barcode[:3:])
print(barcode[::3])
print(barcode[:4:])
print(barcode[::-1])
print(barcode.index("A"))
print(name.split())