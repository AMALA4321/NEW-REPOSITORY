# Ask the user to select investment/bond 
# Save the input to variable selection and convert it to lower case
import math
print("Enter Investment or Bond of which interest to be calculated: ")
selection = input()
selection1 = selection.lower()

#----------------------------------------------------------------------
# If investment is selected,ask the user to enter interest type simple/compound
# If simple interest is selected,total amount=P*(1+(r*t))
if selection1 == "investment":
    print(f"You have selected {selection1}")
    try:
        P = float(input("Enter amount to be deposited: "))
        interest_rate = float(input("Enter interest rate: "))
        r = interest_rate/100
        t = float(input("Enter number of years you plan to invest: "))
        interest = input("Enter interest type you want:simple/compound? ")
        interest = interest.lower()
        if interest == "simple" :
            total_amount = P*(1+(r*t))
            print(f"Amount after {t} years is {round(total_amount,2)}")
# If compound interest is selected,total amount=P*((1+r)**t)
        elif interest == "compound":
            total_amount = P*math.pow((1+r),t)
            print(f"Amount after {t} years is {round(total_amount,2)}")
        else:
            print("Invalid interest type entered")
    except ValueError:
        print("Oops!!!  Value Error!!!  Please enter numerical value")

#--------------------------------------------------------------------
# If bond is selected,repayment=(r*P)/(1-((1+r)**(-n)))
elif selection1 == "bond" :
    print(f"You have selected {selection1}")
    try:
        P = float(input("Enter present value of house: "))
        interest_rate = float(input("Enter interest rate: "))
        r = (interest_rate/100)/12
        n = float(input("Number of months you plan to take to repay the bond:  "))
        repayment = (r*P)/(1-((1+r)**(-n)))
        print(f"Monthly repayment amount {round(repayment,2)}")
    except:
        print("Oops!!!  Value Error!!!  Please enter numerical value")
#------------------------------------------------------------------------

# If user enters any input other than investment,bond; display error
else :
    print("Invalid Input")
    
