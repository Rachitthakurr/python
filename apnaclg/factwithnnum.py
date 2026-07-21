def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)


def con(usd_val):
    inr_val = usd_val * 95
    print(usd_val, "USD = ", inr_val, "INR")

con(1)

con(100)

con(87)



# num function check the avlue is even or odd

def O_or_E(num):
    if num %2 == 0:
        return "Even"
    else:
        return "Odd"
    
num=int(input("enter the number: "))
print(O_or_E(num))
        