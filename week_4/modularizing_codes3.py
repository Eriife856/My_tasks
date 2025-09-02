# class Student:
#     def __init__(self, name, course, level):  # This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created!")
#         # When you create a student, __init__ runs automatically
# kemi = Student("Kemi Adebayo", "Computer Science", 300)

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student object...")
#         self.name = name           # Step 2: Assign name to THIS object
#         self.state_of_origin = state    # Step 3: Assign state to THIS object
#         self.course = course       # Step 4: Assign course to THIS object
#         self.student_id = self.generate_id()  # Step 5: Generate ID for THIS object
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")
    
#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
# # When you create an object, here's what happens:
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# print(ayo.name)        
# print(ayo.student_id)   


# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")
    
#     def buy_airtime(self, amount):
#         self.airtime += amount  # self ensures it goes to the RIGHT person
#         return f"{self.name} now has ₦{self.airtime} airtime"
    
#     # Creating multiple users
# abeeb = PhoneUser( "Abeeb Bakare" , "MTN")     
# onisemo = PhoneUser("Onisemo Williams", "Airtel")  
# # Each person's actions affect only their own account
# print(abeeb.buy_airtime(500))     # Tunde now has ₦500 airtime
# print(onisemo.buy_airtime(1000)) # Blessing now has ₦1000 airtime
# print(abeeb.airtime)              # 500 (Tunde's airtime unchanged)
# print(onisemo.airtime)           # 1000 (Blessing's airtime unchanged)



# # Defining Attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin, cgpa, university):
#         self.name = name                   
#         self.course = course              
#         self.level = level                
#         self.state_of_origin = state_of_origin  
#         self.cgpa = cgpa 
#         self.university = university                
# # Creating a student object
# Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State",4.0,"Federal University of Technology Akure" )
# print(Fathia.name)             
# print(Fathia.course)        
# print(Fathia.state_of_origin)
# print(Fathia.cgpa)
# print(Fathia.university)
# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun", 3.3, "Federal University of Technology Akure")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos", 3.5, "Federal University of Technology Akure")

# print(student1.name) 
# print(student1.course) 
# print(student1.state_of_origin) 
# print(student1.cgpa) 
# print(student1.university)
 
 
# print(student2.name) 
# print(student2.course) 
# print(student2.state_of_origin) 
# print(student2.cgpa) 
# print(student2.university)
# class Student:
#     university = "Federal University of Technology Akure"  
    
#     def __init__(self, name, course):
#         self.name = name         
#         self.course = course

# # print(Student.university)     
# # print(student1.university)   
# # print(student2.university)    


class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False
    

     # Method: action the student can do
    def pay_school_fees(self):                   
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):                   
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
    
      # Method: calculates CGPA
    def calculate_cgpa(self, grades):           
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    # Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())        
print(Abiodun.register_courses())       
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5])) 


# 'self' refers to the specific student
def pay_school_fees(self):  
    return f"{self.name} has paid school fees"

@classmethod
def get_university(cls):
    return cls.university

@staticmethod
def academic_calendar():
    return "Academic session runs from September to July"


class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
    
    # METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
# Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)


# Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")

# Methods (actions)
print(adunni_account.deposit(25000))    
print(adunni_account.withdraw(10000))  
print(adunni_account.transfer(15000, "Sunday James"))  
print(adunni_account.check_balance())  


#attributes
class BRTBus:
    def __init__(self,  route, bus_number):
       
        self.route = "route"            
        self.bus_number = bus_number    
        self.current_stop = "Ikorodu"
        self.passenger_count = 0
        self.fare = 300
    
 #methods
    def announce_stop(self):
        return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"
    
    def board_passengers(self, count):
        self.passenger_count += count
        return f"{count} passengers boarded. Total: {self.passenger_count}"
    
adetoun= ("Adetoun adebisi","ojoo","2342")

print(adetoun.bus_number)
print(adetoun.name)