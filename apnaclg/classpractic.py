#1

class cricle:
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        return (22/7) * self.redius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.redius

c1 = cricle(21)
print(c1.area())
print(c1.perimeter())

#⁡⁢⁣⁣2⁡ 
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role=" , self.role)
        print("dempartment= ", self.department)
        print("salary= ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")


engg1 = Engineer("Pranav" , 21)
engg1.showDetails()
# e1 = Employee("Accountant", "Finance", "60,000")
# e1.showDetails()

# ⁡⁢⁣⁢3⁡
class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, adr2):
        return self.price> adr2.price


odr1 = order("chpis", 20)
odr2 = order("tea", 12)

print( odr1 > odr2)  #⁡⁢⁢⁢true⁡