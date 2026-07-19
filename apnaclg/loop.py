#while loop 
i = 1

while i<=5:
    print("hello")
    i += 1
print("count")

i = 1

while i<=5:
    print("hello", i)
    i += 1
print("count")

#print number from 1 to 100 with while loop

i = 1

while i <= 100:
    print(i)
    i += 1
print("loop is ended")


i = 100

while i >= 1:
    print(i)
    i -= 1
print("loop is ended")

#print the multiplication table of a number n 

n = int(input(" enter the number: "))
i = 1
while i<=10:
    print(n*i)
    i += 1

#print the elment of thr following list using a loop

nums = [1,4,9,16,25,36,49,64,81,100,]
heroes = ["ironman", "spiderman", "venom", "superman"]

idx = 0
i = 0
while idx<=len(nums):
    print(idx)
    idx +=1 
while i<=len(heroes):
    print(heroes,[i])
    break


    