#CREATE A NEW FILE "DEMO.TXT" USING PYTHON. ADD THE FOLLOWING DATA IN IT:
# "Hi everyone
# we are learning filei/o
# using Java
# I like programing in Java.

# with open("demo.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning filei/o\nusing Java\nI like programing in Java.")
#     f.close()

# 2 WAF THAT REPLACE ALL OCCURANCE OF JAVA WITH PYTHON IN A ABOVE FILE.

# with open("demo.txt","r")as f:
#     data = f.read()

# new_data = data.replace("Java" , "Python")
# new_data = data.replace("java" , "Python")
# new_data = data.replace("I" , "i")

# print(new_data)

# with open("demo.txt", "w") as f:
#     f.write(new_data)


# 3 SEARCH IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT?
# def find_word(word):

#  with open("demo.txt","r")as f:
#     data = f.read()
#     if(data.find(word) !=-1):
#         print("found")
#     else:
#        print("Not found")
#  f.close()


# find_word("learning")
# find_word("Python")
# find_word("java")


# 4 WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARING" OCCUR FIRST?

def check_for_word():
    word = "Python"

    with open("demo.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not Found")

# def check_for_line():
#     word ="Python"
#     data = True
#     line_no = 1

#     with open("demo.txt", "r")as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#             return
#         line_no += 1

#     return -1

# print(check_for_line())

def check_for_line():
    word= "Python"

    with open("demo.txt", "r") as f:
        for line_no, line in enumerate(f, start=1):
            if word in line:
                return line_no

    return -1

print(check_for_line())