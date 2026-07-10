a = int(input("enter 1 num: "))
b = int(input("enter 2 num: "))
c = int(input("enter 3 num: "))

if(a>=b and a>=c):
    print("1 num is greatest", a)
elif(b>=c):
    print("2 num is greatest", b)
else:
    print("3 num is greatest",c)