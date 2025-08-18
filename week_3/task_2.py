# print(f"eligible: {eligibility}")
 # federal government scholarship key eligibility
citizenship = input("Are you a citizen of nigeria: ")
enrollment = input("Are you currently enrolled in any tertiary instiution in Nigeria? : ")
other_scholarships = input("Are currently a recepient of any entity in the oil and gas industry?: ")
Academic_qualification = input("kindly input your five core subject along side with the grades: ")

eligibility = ( citizenship == "yes") and (enrollment == "yes") and (other_scholarships == "no") and (Academic_qualification == "A" or "B")
print(f"citizenship: {citizenship}\nenrollment: {enrollment}\nother_scholarship: {other_scholarships}\nacademic_qualification: {Academic_qualification }\nEligibility: {eligibility} ")
