# #task1
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: ")) 
print(f"{num1} =={num2} : {num1 == num2}")
# #explanation
# num1 = 20
# num2 =20
# equal to sign = checks if both numbers are equal
# since num1 is  equals to num2 so it is going to be true

print(f"{num1} != {num2} : {num1 != num2}")
#explanation
# num1 = 25
# num2 =20
# not equal to sign = checks if both numbers are not equal
# since num1 is not equal to num2 so it is going to be true
print(f"{num1} > {num2} : {num1 > num2}")
#explanation
# num1 = 10
# num2= 20
# greater than sign = checks if num1 is greater than num2
# since num1 is not greater than num2 so it is going to be false

print(f"{num1} < {num2} : {num1 < num2}")
#explanation
num1 = 15
num2 = 20
# less than sign = checks if num 1 is less than num2
# since num1 is less than num2 so it is going to be true

# cenarios where i can apply the program above
# To check scores of students in an exam
# To check price of good in a store ( expensive or mmore affordable)
# To check age of a person( minor or adult)
# # writing code for checking the age of a person(minor or adult)
age = int(input("enter your age: "))
eligibility = ( age < 18) or (age > 18)   