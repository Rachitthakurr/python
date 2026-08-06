# class Student:
#     def __init__(self, phy, chem, bio):
#         self.phy = phy
#         self.chem = chem
#         self.bio = bio 


    # def calcculate_percentage(self):
    #     self.percentage = str((self.phy + self.chem + self.bio) / 3) + "%"


    # @property
    # def percentage(self):
    #     return str((self.phy + self.chem + self.bio) / 3) + "%"

        
# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)


#POLYMORPHISM IN PYTHON

# int = "polymorphism in python"
# def upper(string):
#     return string.upper()

# upper = upper(int)
# print(upper)


# ⁡⁢⁢⁢OPERATOR OVERLOADING IN PYTHON⁡
# print(1 + 2) #3 addition
# print(type(1))

# print("rachit" + "Thakur") #concatenate
# print(type("rachit"))
# print([1,2,3] + [4,5,6]) #⁡⁣⁣⁢merge two lists⁡
# print(type([1,2,3]))

class complex:
    def  __init__(self, real, img):
        self.real = real
        self.img = img 

    def showNumber(self):
        print(self.real,"i +", self.img,"j")


    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal , newImg)

num1 = complex(2, 3)
num1.showNumber()

num2 = complex(4, 5)
num2.showNumber()

num3 = num1 + num2  #⁡⁣⁣⁢adding two complex numbers⁡
num3.showNumber()

num4 = num1 - num3  #‍⁡⁣⁣⁢subtracting two complex numbers⁡
num4.showNumber()


