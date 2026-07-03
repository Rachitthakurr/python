item = input("what item would you like to buy: ")
price = input("what is the price of the item: ")
quantity = input("how many items would you like to buy: ")

total = float(price) * int(quantity)
print(f"you have bought {quantity} X {item}(s)")
print(f"the total cost is$: {total}")