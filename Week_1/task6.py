#Electricity bill formatter using escape sequence
customer_name = input("What is your name")
units= input("How many unit do you use per KWh")
units =int(units)
cost = input("What is the cost per unit")
cost =float(cost)
total_bill = units + cost
# receipt= "customer_name:" +customer_name+ "\nunits:"+ units +"\ncost"+ cost+ "."
print(f"customer name: {customer_name}\n total bill: {total_bill} ")
