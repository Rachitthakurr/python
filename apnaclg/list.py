marks = [93.5, 25.2, 34.6, 95.75]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))

student = ["Rachit", 98.5, 20, "Nanauta",]
print(student)
student[2]= 21
print(student)


# # list slicing

list_studdent = [ "rachti", "abhinav", "pranav","okay", "why not", "thik hai ",]
print(list_studdent[1:9])
print(list_studdent[:-1])


# list method

list=[2,3,5,6]
list.append(4)
print(list)

list=[2,3,5,6]
list.append(4)
list.sort()
print(list)

list=[2,3,5,6]
list.append(4)
list.sort(reverse=True)
print(list)

list=[2,3,3,5,6]
list.append(4)
list.pop(3)

print(list)

