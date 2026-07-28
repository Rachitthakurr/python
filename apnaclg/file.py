# f = open("practice.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("practice.txt", "w")
# data = f.write("this is the new line for\nthe file and i'm larning python from apna college i \nidn't get anything from that")
# f.close()

# f = open ("practice.txt","r")
# data = f.read(2)
# print(data)
# f.close()

# f = open("practice.txt" , "r")
# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

# f = open("practice.txt", "a+")
# print(f.read())
# f.write(" abc")
# f.close()

# f = open("practice.txt", "w+")
# print(f.read())
# f.write(" abc")
# f.close()

# WITH Syntax

with open("demo.txt" ,"a+") as f:
    f.seek(0)
    data = f.read()
    print(data)
    
with open("demo.txt", "w") as f:
    f.write("new data")

# DELETE A FILE:
import os
os.remove("demo.txt")


