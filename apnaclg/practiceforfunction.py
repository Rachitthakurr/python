# WAF TO PRINT THE LENGTH OF  A LIST (LIST IS THE PARAMETER)

cities = ["delhi","mumbai","rajisthan","goa","noida","chenni","gurugram"]
heroes = ["superman", "batman", "ironman","spiderman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item, end= " ")
        
print_list(heroes)
print_list(cities)

print()