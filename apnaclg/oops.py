#  ABSTRACTION IN PYTHON 

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluteh = False

    def start(self):
        self.cluteh = True
        self.acc = True
        print("car started..")

    def stop(self):
        self.brk =True
        self.acc = True
        print("car stoped.")

c1 = car()
c1.start()
# c2 = car()
# c2.stop()

# ENCAPSUKATION
# CREATE ACCOUNT CALSS WITH 2 ATTRIBUTE-BALANCE & ACCOUNT NUMBER


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount,"was debited")
        print("total balance= ", self.get_balance())

    def credit(self , amount):
        self.balance += amount
        print("Rs.", amount,"was credited")
        print("total balance= ", self.get_balance())


    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.credit(1000)
acc1.debit(45208)
acc1.credit(5000000)



#  PUBLIC AND PRIVATE ATTRIBUTE


class Account:
    def __init__ (self, acc_on, acc_pass):
        self.acc_on = acc_on
        self.__acc_pass = acc_pass


    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("12345", "abcde")

print(acc1.acc_on)
# print(acc1.__acc_pass)
print(acc1.reset_pass())


#   SIMPLE CLASS FOR PRIVATE 

class Person:
    __name = "noneone"

    def __hello(self):
        print("hello person!")

    def  welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())


#  INHERITANCE TYPE (SINGLE, MULTI-LEVEL INHERITANCE, MULTIPLE INHERITANCE)
#  SINGLE INHERITANCE

class car:

    color ="black"
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluteh = False

    def start(self):
        self.cluteh = True
        self.acc = True
        print("car started..")

    def stop(self):
        self.brk =True
        self.acc = True
        print("car stoped.")

class ToyotaCar(car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.color)
print(car1.start())

#  MULTI-LEVEL INHERITANCE

class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("diesel")
car1.start()

# Multiple Inheritance

class A:
    varA ="welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)



# SUPER METHON IN INHERITANCE

class car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Fortuner", "petrol")
print(car1.name)
print(car1.type)


# CLASS METHOD IN PYTHON

class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name
        Person.name = name #instead of self.name we can use class name to change the value of class attribute
        self.__class__.name = "rachit" #instead of self.name we can use class name to change the value of class attribute


    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahit Thakur")
print(p1.name)
print(Person.name)