# Description: Python QAP 4 - Program for One Stop Insurance Company to enter and calculate new insurance policies
# Author: Cody Collins
# Date(s): July 17, 2024 - 
 
 
# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants.
with open("Const.dat", 'r') as f:
    for line in f:
        ConstLst = line.split(",")

        PolicyNum = int(ConstLst[0].strip())
        BASIC_PREMIUM = float(ConstLst[1].strip())
        ADD_CARS_DISC = float(ConstLst[2].strip())
        EXT_LIAB_COST = float(ConstLst[3].strip())
        GLASS_COV_COST = float(ConstLst[4].strip())
        LOANER_COST = float(ConstLst[5].strip())
        HST_RATE = float(ConstLst[6].strip())
        PROC_FEE = float(ConstLst[7].strip())

# Define program functions.



# Main program starts here.
while True:
    while True:
        CustFName = input("Enter the customer's first name: ").title()
        if CustFName == "":
            print("ERROR - First name cannot be blank.")
        else:
            break

    while True:
        CustLName = input("Enter the customer's last name: ").title()
        if CustLName == "":
            print("ERROR - Last name cannot be blank.")
        else:
            break

    while True:
        CustStAdd = input("Enter the customer's street address: ")
        if CustStAdd == "":
            print("ERROR - Street address cannot be blank.")
        else:
            break

    while True:
        CustCity = input("Enter the customer's city: ").title()
        if CustCity == "":
            print("ERROR - City cannot be blank.")
        else:
            break
    
    ProvLst = ["NL", "NS", "PE", "NB"]
    while True:
        CustProv = input("Enter the customer's province(NL, NS, PE, NB): ").upper()
        if CustProv == "":
            print("ERROR - Province cannot be blank.")
        elif len(CustProv) != 2:
            print("ERROR - Province must be 2 characters.")
        elif CustProv not in ProvLst:
            print("ERROR - Province not valid.")
        else:
            break

    while True:
        CustPostCode = input("Enter the customer's postal code(X9X9X9): ")
        if CustPostCode == "":
            print("ERROR - Postal code cannot be blank.")
        elif len(CustPostCode) != 6:
            print("ERROR - Postal code must be 6 characters.")
        else:
            break
    
    allowed_char1 = ("1234567890")
    while True:
        CustPhone = input("Enter the customer's phone number(9999999999): ")
        if CustPhone == "":
            print("ERROR - Phone number cannot be blank.")
        elif len(CustPhone) != 10:
            print("ERROR - Phone number must be 10 characters.")
        elif set(CustPhone).issubset(allowed_char1) == False:
            print("ERROR - Phone number must contain only numbers.")
        else:
            break
    
    while True:
        NumCars = int(input("Enter the number of cars being insured: "))
        if NumCars <= 0:
            print("ERROR - Number of cars must be a positive integer.")
        else:
            break
    
    while True:
        ExtLiability = input("Does the customer require extra liabililty up to $1,000,000(Y/N): ").upper()
        if ExtLiability == "":
            print("ERROR - Response cannot be blank.")
        else:
            break
    
    while True:
        GlassCover = input("Does the customer require glass coverage(Y/N): ").upper()
        if GlassCover == "":
            print("ERROR - Response cannot be blank.")
        else:
            break

    while True:
        LoanCar = input("Does the customer require a loaner car(Y/N): ").upper()
        if LoanCar == "":
            print("ERROR - Response cannot be blank.")
        else:
            break
    
    PayMethodLst = ["Full", "Monthly", "Down Pay"]
    while True:
        PayMethod = input("Enter the payment method(Full, Monthly, or Down): ").title()
        if PayMethod == "":
            print("ERROR - Payment method cannot be blank.")
        elif PayMethod not in PayMethodLst:
            print("ERROR - Payment method not valid.")
        elif PayMethod == "Down Pay":
            DownPayAmt = float(input("Enter the down payment amount: "))
        else:
            break

    

    
    




# Any housekeeping duties at the end of the program.