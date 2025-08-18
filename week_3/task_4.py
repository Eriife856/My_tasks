student ={}
student_name= input("enter your name: ")
age= int(input("enter your age: "))
score = int(input("enter your score: g"))

student["scores"] = [50,60,70,80]
student['passed'] = sum(student["scores"])/len(student["scores"])>=50
student["teengers"] = age >=13 and age <=19
print(student)

