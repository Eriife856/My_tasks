#name organizer
name= input("kindly input name separated by spaces: ")
name_list = name.lower().split()
for name in name_list: 
    name_list.sort()
    print(f"{name}\n")
