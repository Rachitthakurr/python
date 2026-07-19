x = y = z ="hello"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

x = "python is awesome"
print(x)

x = "python "
y = "is "
z = "awesome"
print(x+y+z)

x = 5 
y = 67
print(x+y)

x = "rachit"
y = 56
print(x,y)

x = "awesome"

def func():
    print("python is " + x)

func()

x = "awesome"

def func():
    x = "fantastic"
    print("python is " + x)

func()

print("python is " + x)


def func():
    global x
    x ="fantastic"

func()

print("python is " + x)     



x = "awesome"

def func():
    global x
    x ="fantastic"

func()

print("python is " + x)