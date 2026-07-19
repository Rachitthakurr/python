tup = ( 1,3,2,3,44)
for num in tup:
    print(num)

str = "Rachit Thakur"
for char in str:
    print(char)
else:
    print("end")


str = "Rachit Thakur"
for char in str:
    if(char == 'T'):
        print("o found")
        break
    print(char)
else:
    print("end")

#print the element of the following list a loop

nums =[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)


#search for a number x in this tuple using loop

nums = (1,4,9,16,25,36,49,64,81,100)
x = 9
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx += 1