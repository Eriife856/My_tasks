# #Create and display
# fav_dish1 = input("Kindly enter ypour favourite dish: ")
# fav_dish2 = input("Kindly enter ypour favourite dish: ")
# fav_dish3 = input("Kindly enter ypour favourite dish: ")
# fav_dishes=(fav_dish1,fav_dish1, fav_dish1 )
# print(fav_dishes)
# print(f"{fav_dish1}\n{fav_dish2}\n{fav_dish3}")



# #tuple and input
# #task2
# best_friend1= input("Kindly input your best_friend'name:")
# best_friend2= input("Kindly input your best_friend'name:")
# best_friend3=input("Kindly input your best_friend'name:")
# best_friend4=input("Kindly input your best_friend'name:")
# best_friend5=input("Kindly input your best_friend'name:") 
# best_friend =(best_friend1,best_friend2,best_friend3,best_friend4,best_friend5)
# print(best_friend) 
# print(best_friend[::-1])



# #tuple operation 
# #task 3
# nigerian_state1  = input("kindly enter state in nigeria:")
# nigerian_state2 = input("kindly enter state in nigeria:")
# nigerian_state3 = input("kindly enter state in nigeria:")
# nigerian_state4 = input("kindly enter state in nigeria:")
# nigerian_state5 = input("kindly enter state in nigeria:")
# nigerian_states=(nigerian_state1,nigerian_state2 ,nigerian_state3 ,nigerian_state4 ,nigerian_state5  )
# print(nigerian_states)
# print(nigerian_states[0])
# print(nigerian_states[4])
# nigerian_states=("lagos")
# print("lagos" in nigerian_states)
# print(f"{len(nigerian_states)}")


# #tuple unpacking
# #task4
# first_name=input("kindly input your first name : ")
# age =input("input your age:")
# favorite_colour=input("kindly input your favourite colour:")
# home_town=input("kimdly input your home_town:")
# information= (f"{first_name}\n{age}\n{favorite_colour}\n{home_town}")
# print(information)


#Modify tuple indirectly
#task5
shopping_list1 =input("kindly enter your shopping list:")
shopping_list2 =input("kindly enter your shopping list:")
shopping_list3 =input("kindly enter your shopping list:")
shopping_list=(shopping_list1,shopping_list2,shopping_list3)
print(shopping_list)
lst=list(shopping_list)
items_1=input("kindly pprovide other items: ")
items_2=input("kindly provide other items:")
new_list=(f"{items_1},{items_2}")
print(new_list)
# lst2=list(new_list)
lst.append(new_list)
print(lst)
shopping_list=tuple(lst)
print(shopping_list)

#Attendence tracker
#tasks6
weekdays=("monday","tuesday","wednesday","thursday","friday")
months=("january","feburary","march","april","may","july","august","september","octomber","november","december")
students_name =input("kindly input your name: ")
gender =input("kindly input your gender:")
course_track =input("provide your course_track")
current_month_number=int(input("kindly input month number(1-12):" ))
current_day_number= int(input("kindly input day number(1-7): "))
print("\n  attendence tracker   ")
print(f"student_name {students_name}")
print(f"gender: {gender}")
print(f"course_track: {course_track}")
print(f"current_month_number:{current_month_number}")
print(f"current_day_number:{current_day_number}")