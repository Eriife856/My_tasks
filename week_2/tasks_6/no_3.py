# simulate a football match ticket system
# storing number 1-50 in sets using range
seat_number =set(range(1,50))
#asking user to book a set by entering seat number
seat_number1 = int(input("kindly book a seat number:"))
seat_number2 = int(input("kindly book a seat number:"))
seat_number3 = int(input("kindly book a seat number:"))
seat_number4 = int(input("kindly book a seat number:"))
#remove booked seats from set using .remove
seat_number.remove(seat_number1 )
seat_number.remove(seat_number2 )
seat_number.remove(seat_number3 )
seat_number.remove(seat_number4 )
print(seat_number)