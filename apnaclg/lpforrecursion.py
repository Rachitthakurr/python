#write a recursion function the sum of first n number

def cal_sum(n):
    if(n==0):
        return 0
    print(n)
    cal_sum(n-1)

cal_sum(5)


def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n - 1)+ n

sum = calc_sum(5)
print(sum)


# WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENT INA LIST
#HINT : USE LIST AND IDX AS A PARAMETER

def print_list(list , idx=0):
    if( idx == len(list)):
        return
    print(list[idx], end=" ")
    print_list(list , idx + 1)

fruits = ["banana", "mango", "apple", "Banana"]
print_list(fruits)