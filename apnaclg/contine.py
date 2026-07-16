i = 0 
while i <= 5:
    print(i)
    i +=1


i = 0 
while i<= 5:
    if(i == 3): # 3 ko skip kar diya hai continue use kar ka
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i<= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i<= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1

