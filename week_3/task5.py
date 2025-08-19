# store inventory
store = {"textbooks": 10, "pens": 20, "notebooks": 15}
# function to display inventory
choice = input("what do you want to buy:  ")
quantity = int(input("how many do you want to buy:  "))
store[choice] -= quantity
# "-=" subtracts the quantity from the store
print(store)