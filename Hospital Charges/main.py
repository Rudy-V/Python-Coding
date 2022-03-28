# In-patient function
def inPatient(num_day=0,daily_rate=0,medication_charge=0,hos_services=0):
    '''Arguments: 
    The number of days spent in the hospital,
    The daily rate,
    Hospital medication charges,
    Charges for hospital services (lab tests etc)'''
    return round(float((num_day*daily_rate)+medication_charge+hos_services),2)

# Out-patient function
def outpatient(medication_charge=0,hos_services=0):
    '''Arguments:
    Hospital medication charges,
    Charges for hospital services (lab tests etc)'''
    return round(float(medication_charge+hos_services),2)

# Asks the user for input and calls the relevant function
print('''
Welcome to the hospital charge calculator:
Press -1 to exit
================================================================
''')

user_input = ""

while user_input != "-1":
    
    user_input = str(input("Please enter 'In' for in-patients or 'Out' for out patients: "))

    if user_input == "In":
        print("Please enter the following information: ")
        days = int(input("The number of days the patient was in the hospital: "))
        day_rate = float(input("The daily rate: "))
        medication = float(input("The medicine charge: "))
        hospital_services = float(input("The charge for hospital services: "))
        print(f"The total charge is: R{inPatient(days,day_rate,medication,hospital_services)}")
        print("================================================================")

    elif user_input == "Out":
        print("Please enter the following information: ")
        medication = float(input("The medicine charge: "))
        hospital_services = float(input("The charge for hospital services: "))
        print(f"The total charge is: R{outpatient(hospital_services,medication)}")
        print("================================================================")

    else:
        print("Invalid input")
        print("================================================================")
