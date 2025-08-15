# create a unique voters registration system
voter_name1 =input("kindly enter your name:")
voter_name2= input("kindly enter your name:")
voter_name3= input("kindly enter your name:")
voter_name4= input("kindly enter your name:")
voters = set()
for voter in [voter_name1, voter_name2,voter_name3 ,voter_name4]:
    if voter in voters:
        print(f"warning {voter} is already restricted.") 
    else:
        voters.add(voter)
print("\ntotal number of voters:",len(voters))



