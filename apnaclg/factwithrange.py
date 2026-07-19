#wap to find the sum of first n natural number (using while & for loop)

#for loop

# n = 5
# sum = 1
# for i in range(1, n+1):
#     sum *= i
# print("total sum= ", sum)

#while loop

# n = 5
# sum = 1
# i = 1
# while i<=n:
#     sum *= i 
#     i += 1
# print("total sum = ", sum)


#wap to find the factotial of first n number using for loop

# while loop

# n = 5
# fact = 1 
# i = 1
# while i<= n:
#     fact *= i
#     i += 1
# print("factorial = ", fact )

# for loop 

# n = 5 
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("factorial = ",fact)


n = 120
fact = 1
i = 1
while i <= n:
    fact *=i
    i += 1
print(fact)