
with open("file3.txt","r+") as myfile:
    myfile.write("We are fine")
    print(myfile.read())
myfile.close()