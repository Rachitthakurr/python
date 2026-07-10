name = "rachit thakur"
age = 20 
gpa = 8.25
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

age = str(age)
age += "1"

print(age)

print(age)

marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks <80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->", grade)

