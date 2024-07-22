# Description: Python QAP 4 - Program for One Stop Insurance Company to enter and calculate new insurance policies
# Author: Cody Collins
# Date(s): July 17, 2024 - 
 
 
# Define required libraries.
import datetime
import FormatValues as FV
import sys
import time 


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

def Ext_Costs(NumCars, ExtLiability, GlassCover, LoanCar, EXT_LIAB_COST, GLASS_COV_COST, LOANER_COST):
    # calculate the extra costs
    ExtLiabFee = 0
    if ExtLiability == "Y":
        ExtLiabFee = EXT_LIAB_COST * NumCars
    
    GlassCovFee = 0
    if GlassCover == "Y":
        GlassCovFee = GLASS_COV_COST * NumCars

    LoanerFee = 0
    if LoanCar == "Y":
        LoanerFee = LOANER_COST * NumCars
    
    TotExtCost = ExtLiabFee + GlassCovFee + LoanerFee

    return TotExtCost

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


# Main program starts here.
while True:
    while True:
        CustFName = input("Enter the customer's first name: ").title()
        if CustFName == "":
            print()
            print("ERROR - First name cannot be blank.")
            print()
        else:
            break

    while True:
        CustLName = input("Enter the customer's last name: ").title()
        if CustLName == "":
            print()
            print("ERROR - Last name cannot be blank.")
            print()
        else:
            break

    while True:
        CustStAdd = input("Enter the customer's street address: ")
        if CustStAdd == "":
            print()
            print("ERROR - Street address cannot be blank.")
            print()
        else:
            break

    while True:
        CustCity = input("Enter the customer's city: ").title()
        if CustCity == "":
            print()
            print("ERROR - City cannot be blank.")
            print()
        else:
            break
    
    ProvLst = ["NL", "NS", "PE", "NB"]
    while True:
        CustProv = input("Enter the customer's province(NL, NS, PE, NB): ").upper()
        if CustProv == "":
            print()
            print("ERROR - Province cannot be blank.")
            print()
        elif len(CustProv) != 2:
            print()
            print("ERROR - Province must be 2 characters.")
            print()
        elif CustProv not in ProvLst:
            print()
            print("ERROR - Province not valid.")
            print()
        else:
            break

    while True:
        CustPostCode = input("Enter the customer's postal code(X9X9X9): ")
        if CustPostCode == "":
            print()
            print("ERROR - Postal code cannot be blank.")
            print()
        elif len(CustPostCode) != 6:
            print()
            print("ERROR - Postal code must be 6 characters.")
            print()
        else:
            break
    
    allowed_char1 = ("1234567890")
    while True:
        CustPhone = input("Enter the customer's phone number(9999999999): ")
        if CustPhone == "":
            print()
            print("ERROR - Phone number cannot be blank.")
            print()
        elif len(CustPhone) != 10:
            print()
            print("ERROR - Phone number must be 10 characters.")
            print()
        elif set(CustPhone).issubset(allowed_char1) == False:
            print()
            print("ERROR - Phone number must contain only numbers.")
            print()
        else:
            break
    
    while True:
        NumCars = int(input("Enter the number of cars being insured: "))
        if NumCars <= 0:
            print()
            print("ERROR - Number of cars must be a positive integer.")
            print()
        else:
            break
    
    while True:
        ExtLiability = input("Does the customer require extra liabililty up to $1,000,000(Y/N): ").upper()
        if ExtLiability == "":
            print()
            print("ERROR - Response cannot be blank.")
            print()
        else:
            break
    
    while True:
        GlassCover = input("Does the customer require glass coverage(Y/N): ").upper()
        if GlassCover == "":
            print()
            print("ERROR - Response cannot be blank.")
            print()
        else:
            break

    while True:
        LoanCar = input("Does the customer require a loaner car(Y/N): ").upper()
        if LoanCar == "":
            print()
            print("ERROR - Response cannot be blank.")
            print()
        else:
            break
    
    PayMethodLst = ["Full", "Monthly", "Down Pay"]
    while True:
        PayMethod = input("Enter the payment method(Full, Monthly, or Down pay): ").title()
        if PayMethod == "":
            print()
            print("ERROR - Payment method cannot be blank.")
            print()
        elif PayMethod not in PayMethodLst:
            print()
            print("ERROR - Payment method not valid.")
            print()
        else:
            break
    if PayMethod == "Down Pay":
        DownPayAmt = float(input("Enter the down payment amount: "))

    # Perform required calculations

    if NumCars == 0:
        PremCost = BASIC_PREMIUM
    else:
        PremCost = BASIC_PREMIUM + ((NumCars * BASIC_PREMIUM) * ADD_CARS_DISC)

    TotExtCost = Ext_Costs(NumCars, ExtLiability, GlassCover, LoanCar, EXT_LIAB_COST, GLASS_COV_COST, LOANER_COST)

    TotPrem = PremCost + TotExtCost

    HSTCost = TotPrem * HST_RATE

    TotCost = TotPrem + HSTCost

    MonPay = (TotCost + PROC_FEE) / 8
    if PayMethod == "Down Pay":
        MonPay = ((TotCost - DownPayAmt) + PROC_FEE) / 8

    InvDate = datetime.datetime.now()
    InvDateDsp = FV.FDateS(InvDate)
    

    FirstPayYear = InvDate.year
    FirstPayMonth = InvDate.month
    FirstPayDay = 1

    FirstPayDate = datetime.date(FirstPayYear, FirstPayMonth + 1, FirstPayDay)
    

    # display results
    FullName = CustFName + " " + CustLName
    if ExtLiability == "Y":
        ExtLiability = "YES"
    else: 
        ExtLiability = "NO"
    if GlassCover == "Y":
        GlassCover = "YES"
    else: 
        GlassCover = "NO"
    if LoanCar == "Y":
        LoanCar = "YES"
    else:
        LoanCar = "NO"

    CustPhDsp = FV.FPhone(CustPhone)

    print()
 
    TotalIterations = 30 
    Message = "Saving Claim Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()

    f = open("Policies.dat", "r")

    print()
    print(f"                     One Stop Insurance Company")
    print(f"                         New Policy Receipt")
    print(f"====================================================================")
    print(f"Customer name: {FullName:<20s}")
    print(f"Address:       {CustStAdd:<20s}") 
    print(f"               {CustCity}, {CustProv:<2s} {CustPostCode:<9s}")
    print(f"Phone:         {CustPhDsp}")
    print(f"Policy number: {PolicyNum:<4d}")
    print(f"--------------------------------------------------------------------")
    print(f"Number of cars to insure: {NumCars:<2d}")
    print(f"Extra liability:          {ExtLiability:<3s}")
    print(f"Glass coverage:           {GlassCover:<3s}")
    print(f"Loaner car:               {LoanCar:<3s}")
    print(f"Payment method:           {PayMethod:<8s}")
    print(f"--------------------------------------------------------------------")
    print(f"Premium cost:       {FV.FDollar2(PremCost):<9s}")
    print(f"Extra costs:        {FV.FDollar2(TotExtCost):<9s}")
    print(f"--------------------------------------------------------------------")
    print(f"Total premium cost: {FV.FDollar2(TotPrem):<9s}")
    print(f"HST:                {FV.FDollar2(HSTCost):<7s}")
    print(f"Total cost:         {FV.FDollar2(TotCost):<9s}")
    print(f"Montly payment:     {FV.FDollar2(MonPay):<9s}")
    print(f"--------------------------------------------------------------------")
    print(f"First payment due: {FirstPayDate}")
    print(f"====================================================================")
    print()
    print(f"Previous policies:")
    print(f"Policy #         Date         Total cost")
    print(f"----------------------------------------")
    for Policies in f:

        # read the record and grab values.
        PolicyLst = Policies.split(",")
        PolicyNumOld = PolicyLst[0].strip()
        InvDateOld = PolicyLst[1].strip()
        TotCostOld = PolicyLst[2].strip()


        print(f"{PolicyNumOld:<4s}          {InvDateOld:<10s}      ${TotCostOld:<9s}\n")
         
    f.close()

    print(f"====================================================================")
    print()
    # increment policy number

    PolicyNum += 1


    # write data to file
    f = open("Policies.dat", "a")
    f.write(f"{PolicyNum}, {InvDateDsp}, {TotCost}\n")
    f.close()



# Any housekeeping duties at the end of the program.
    print()
    Continue = input("Would you like to enter another policy? (Y/N): ").upper()
    if Continue == "N":
        break
    print()

# update the constants file
f = open("Const.dat", "w")
f.write(f"{PolicyNum}, {BASIC_PREMIUM}, {ADD_CARS_DISC}, {EXT_LIAB_COST}, {GLASS_COV_COST}, {LOANER_COST}, {HST_RATE}, {PROC_FEE} \n")
f.close()
