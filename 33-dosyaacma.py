# myFile=open("myFile.txt")
# print(type(myFile))
# print(myFile.read())
# print(myFile.read())
# print(myFile.seek(0))
# print(myFile.read())
# myFile.close()

# with open("myFile.txt") as myFile:
#     myContent=myFile.read()

# print(myContent)

# with open("myFile.txt",mode="w") as myFile:
#     myFile.write("test1")
# print(myFile)

# with open("myFile.txt" ,mode="r") as myFile2:
#     myContent=myFile2.read()
# print(myContent)

#w--write r--read a--append

with open("myFile.txt",mode="a") as myNewFile:
    myNewFile.write("sumos")
with open("myFile.txt" ,mode="r") as myNewFile2:
    myContent=myNewFile2.read()
print(myContent)


