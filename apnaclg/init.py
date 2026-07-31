# class student:
#     name ="Rachit Thakur"

# s1 = student()
# print(s1.name)


# class car:
#     name="BMW"
#     color="GREY"

# c1 = car()
# print(c1.name)
# print(c1.color)

#INIT FUNCTION IN PYTHON

# class student:
#     def __init__(self,name):
#         self.name = name

# s1 =student("Rachit Thakur")
# print(s1.name)

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.mark = marks
#         print("adding new student inthe databass")

# s1 = student("Abhinav Choudhary", 78)
# print(s1.name, s1.mark)
# s2 = student("Rachit Thakur", 86)
# print(s2.name,s2.mark)


# CLASS & INSTANCE {ATTRIBUTE}

# class student:
#     college_name = "ABC COLLEGE"
#     # name ="anonymous"#class attribute

#     def __init__ (self, name, marks):
#         self.name = name #object attribute > class attribute
#         self.mark = marks
#     def welcome(self):
#         print("welcome student," , self.name)

#     def get_marks(self):
#         return self.mark

# s1 = student("karan", 97)
# s1.welcome()
# print(s1.get_marks())

class student:
    def __init__ (self, name,marks):
        self.name = name 
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name,"your avg score is: ", sum/3)

s1 =student("tony stark",[99,44,77])
s1.get_avg()
