# This program does following internet banking operations
# 1. OPEN NEW DEPOSIT
# 2. MODIFY ACCOUNT DETAILS
# 3. FUND TRANSFER BETWEEN ACCOUNTS
# 4. SHOW ALL ACCOUNTS DETAILS
# 5. BALANCE ENQUIRY
# 6. PASSWORD CHANGE
# 7. SIGNUP AND LOGIN
# 8. CLOSE EXISTING DEPOSIT

import pickle # TO SERIALIZE AND DE-SERIALIZE PYTHON OBJECT
import os # TO INTERACT WITH OS ,MANAGEMENT OF FILES AND DIRECTORIES
import pathlib # FOR HANDLING FILES AND PATHS ON YOUR OS
import datetime
from datetime import date
import pandas as pd
import random
import math

# A CLASS Account IS CREATED
class Account :
    cif_id = ""
    accNo = 0
    name = ""
    deposit= 0
    balance = 0
    acc_type = ""
    address = ""
    dob = ""
    phone_no = " "
    open_date = " "
    maturity_date = ""
    email_id = " "
    gender = ""
    password = ""
    int_type = ""
    interest_rate = 0
    maturity_amount = 0
    period = 0

#******************************************************************************   
#******************************************************************************
# WELCOME SCREEN   
def intro():
   print("\t\t\t\t**********************")
   print("\t\t\t\t\tWELCOME")
   print("\t\t\t\t**********************")
   print("\t\t\t\tONLINE BANKING PORTAL")
   print("\t\t\t\t\tABC BANK ")
   print("\t\t\t\t**********************")
   print("SELECT WHAT YOU WANT TO DO:")
   print()
   print(" 1 for sign in")
   print(" 2 for sign up")
   print()
   selection = input()
   if selection == '1' or selection == '2':
       return selection
   else:
       print("Invalid selection.Please try again")
       intro()

# FUNCTION TO DISPLAY MENU AND CALL APPROPRIATE FUNCTIONS BASED ON USER INPUT
def display_menu(num) :
    ch = 0
    while ch != 8 :
           print()
           print("\t MAIN MENU")
           print("\t***********")
           print("\t1. OPEN NEW DEPOSIT")
           print("\t2. TRANSFER AMOUNT")
           print("\t3. BALANCE ENQUIRY")
           print("\t4. ALL ACCOUNTS")
           print("\t5. CLOSE DEPOSIT")
           print("\t6. MODIFY ACCOUNT DETAILS")
           print("\t7. CHANGE PASSWORD")
           print("\t8. EXIT")
           print()
           print("\tSelect Your Option (1-8) ")
           ch = input()
           if ch == '1':
               new_deposit(num)
           elif ch =='2':
               num2 = input("Enter account to which amount to be transferred : ")
               if check_if_account_exists(num2):
                    transfers(num,num2)
               else:
                    print("Wrong account number entered")
          
           elif ch == '3':
               balance_inquiry(num)
           elif ch == '4':
               all_accounts(num)
           elif ch == '5':
               num2 = input("Enter deposit account to be closed: ")
               deleteAccount(num2)
               
           elif ch == '6':
               modifyAccount(num)
           elif ch == '7' :
               password_change(num)
           elif ch == '8':
               print("\tThanks for using bank management system")
               break
           else :
               print("Invalid choice")  

# SIGNUP AND OPENS NEW ACCOUNT FOR NEW CUSTOMER             
def signup():
    account = Account()
    account.email_id = check_mail_id()
    flag = 0
    password_1 = new_password_new_user()
    password_2 = input("Re renter your password : ") 
    if password_1 == password_2 :
        account.password = password_1
        flag = 1
        account.name = input("Enter your name : ")
        account.acc_type = check_account_type()
        account.gender = input("Enter your gender : ")
        account.address = input("Enter your address: ")
        account.dob = input("Enter your date of birth: ")
        account.deposit = check_initial_amount()
        account.phone_no = check_phone_no()
        account.accNo = generate_account_no()
        account.cif_id = generate_cif_id()
        account.open_date = datetime.date.today()
        print()     
        print(f"Your account number is {account.accNo} and customer id {account.cif_id}")
        print("Thank you for opening account with us")
        writeAccountsFile(account)
    else:
        print("passwords do not match! Try again")
           
# CHECK IF MAIL ID ENTERED IS CORRECT
def check_mail_id() :
    mail_id = input("Enter your mail id: ")
    if '@' in mail_id  and '.com' in mail_id :
            return mail_id
    else:
            print("Enter valid email id ")
            check_mail_id()
    

# CHECK IF CORRECT ACCOUNT TYPE ENTERED
def check_account_type() :
    acc_type = input("Enter type of account [Current/Savings] you wish to open : ")
    acc_type = acc_type.lower()
    if acc_type == 'savings' or  acc_type == 'current' :
        return acc_type
    else :
        print("Invalid account type entered!!Try again")
        check_account_type()

# CHECK IF PHONE NO ENTERED IS CORRECT
def check_phone_no() :
    phno = input("Enter your phone number: ")
    if len(phno) == 10 and phno.isdigit() :
        return phno
    else:
        print(" phone number to be 10 digits long and contains only digits .Try again")
        check_phone_no()

# CHECK IF INITIAL AMOUNT ENTERED IS AS PER REQUIREMENT     
def check_initial_amount() :
    initial_amount = float(input("Enter Initial deposit amount(>=10)"))
    if initial_amount >= 10 :
        return  initial_amount 
    else:
        print("Initial amount should be greater than 10 .Try again") 
        check_initial_amount()

# CREATES PASSWORD FOR NEW USER
def new_password_new_user():
        val = False
        while val != True:
            val = True
            print("Create your password")
            print()
            pwd = input("password should be minimum of 8 characters long,contains atleast a digit and a special character ")
            special_char_list ='[!$%^&*()_-+={~#@;:/?.>,<}]'
        
            if len(pwd) < 6 :
                print('length should be at least 6')
                val = False
            if len(pwd) > 20 :
                print('length should be not be greater than 8')
                val = False
            if not any(char.isdigit() for char in pwd) :
                print('Password should have at least one numeral')
                val = False
            if not any(char.isupper() for char in pwd) :
                print('Password should have at least one uppercase letter')
                val = False
            if not any(char.islower() for char in pwd) : 
                print('Password should have at least one lowercase letter')
                val = False
            if not any(char in special_char_list for char in pwd) :
                print('Password should have at least one special character')
                val = False
        
        return pwd
   
# FUNCTION TO CREATE NEW ACCOUNT
def writeAccount() :
    account = Account()   
    account.type = input("Enter type of account [Current/Savings] you wish to open : ")
    account.deposit = int(input("Enter Initial deposit amount(>=500 for Saving and >=1000 for current"))
    account.accNo = generate_account_no()
    print(f"\n\n\nAccount Created. Your account number is {account.accNo}")
    writeAccountsFile(account)

# writing account details to data file
def writeAccountsFile(account) :  
   file = pathlib.Path("accounts.data")
   if file.exists () :
       infile = open('accounts.data','rb')
       oldlist = pickle.load(infile)
       oldlist.append(account) # ALL ACC DETAILS IN OLDLIST
       infile.close()
       os.remove('accounts.data')
   else :
       oldlist = [account]
   outfile = open('newaccounts.data','wb')
   pickle.dump(oldlist, outfile)#SOURCE,DESTINATION
   outfile.close()
   os.rename('newaccounts.data', 'accounts.data') 

# 1. CREATE NEW DEPOSIT ACCOUNT
def new_deposit(num) :
    account = Account()
    file = pathlib.Path("accounts.data")
    if file.exists () :
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
               account.cif_id = item.cif_id
               if item.acc_type == "savings":
                   sbacc = item
                   
    try :
        account.deposit = float(input("Enter amount to be deposited: "))
        account.interest_rate = 5
        account.acc_type = "deposit"
        account.open_date = datetime.date.today()
        r = 5/100
        t = float(input("Enter number of years you plan to invest: "))
        account.maturity_date = account.open_date + pd.DateOffset(years=t)
        interest = input("Enter interest type you want:simple/compound? ")
        interest = interest.lower()
        # If amount to be deposited > account balance, display error
        if sbacc.deposit >= account.deposit:
            sbacc.deposit = sbacc.deposit-account.deposit
            print(sbacc.deposit)
            account.name = sbacc.name
            # Deposit maturity calculated if interest type is simple
            if interest == "simple" :
                total_amount = account.deposit*(1+(r*t))
                account.maturity_amount = round(total_amount,2)
                account.period = t
                account.int_type ='simple'
                account.accNo = generate_account_no()
                print()
                print(f"\t\t\tDeposit Details ")
                print("**************************************************************************")
                print(f"Your deposit number is {account.accNo}    Amount {account.deposit}")
                print()
                print(f"Deposited for {t} years        Open Date: {account.open_date}               Maturity Date: {account.maturity_date}")
                print()
                print(f"Interest rate:{account.interest_rate}% ({account.int_type} interest)        Maturity amount: {round(total_amount,2)} ")
                print("****************************************************************************")
                oldlist.append(account)
                #writeAccountsFile(account)
           
            # If compound interest is selected,total amount=P*((1+r)**t)
            elif interest == "compound":
                total_amount = account.deposit*math.pow((1+r),t)
                account.maturity_amount = round(total_amount,2)
                account.period = t
                account.int_type ='compound'
                account.accNo = generate_account_no()
                print()
                print(f"\t\t\tDeposit Details ")
                print("*******************************************************************")
                print(f"Your deposit number is {account.accNo}      Amount {account.deposit}")
                print()
                print(f" Deposited for {t} years       Open Date: {account.open_date}        Maturity Date: {account.maturity_date}")
                print()
                print(f"Interest rate:{account.interest_rate}% ({account.int_type}interest)  Maturity amount: {round(total_amount,2)} ")
                print("****************************************************************************")
                print()
                oldlist.append(account)
            
            else:
                print("Invalid interest type entered")
        else:
            print("Insufficient balance!!!")
    except ValueError:
         print("Oops!!!  Value Error!!!  Please enter numerical value")
         
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

# TO GENERATE RANDOM ACCOUNT NUMBER   
def generate_account_no() :
    random_num = random.randint(0, 1000)
    account_num = 100000 + random_num
    return account_num

# TO GENERATE RANDOM CUSTOMER ID
def generate_cif_id() :
    random_num = random.randint(0, 1000)
    cif_id = 200000 + random_num
    return cif_id
    
# TO DO FUND TRANSFERS
def transfers(num1,num2):
   file = pathlib.Path("accounts.data")
   if file.exists ():
       infile = open('accounts.data','rb')
       mylist = pickle.load(infile)
       infile.close()
       os.remove('accounts.data')# DELETE THE FILE
       try: 
         for item in mylist :
            if item.accNo == num1 :
                amount = int(input("Enter the amount to deposit : "))
                if item.deposit >= amount :
                    for  i in mylist :
                      if (int(i.accNo) == int(num2)) :
                        i.deposit += amount
                      
                    item.deposit = item.deposit - amount
                    print("Your balance is updated")
                    print(f"Your account balance is : {item.deposit}")                        
                else :
                       print("Insufficient balance")   
                       print(f"Your account balance is : {item.deposit}")  
       except :
              print("enter amount in numerals")
                                              
   else :
       print("No records to Search")
   outfile = open('newaccounts.data','wb')
   pickle.dump(mylist, outfile)# writes data to file 
   outfile.close()
   os.rename('newaccounts.data', 'accounts.data')# newaccounts.data renamed as accounts.data  
   
#  BALANCE ENQUIRY
def balance_inquiry(num) :
   file = pathlib.Path("accounts.data")
   if file.exists () :
       infile = open('accounts.data','rb')
       mylist = pickle.load(infile)
       infile.close()
       found = False
       for item in mylist :
           if item.accNo == num :
               print("Your account Balance is = ",item.deposit)
               found = True
   else :
       print("No records to Search")
   if not found :
       print("No existing record with this number")

#  TO DISPLAY ALL ACCOUNT DETAILS OF THE CUSTOMER
def all_accounts(num) :
   file = pathlib.Path("accounts.data") #  FILE PATH OF FILE WITH NAME ACCOUNTS.DATA SAVED TO VARIABLE FILE
   if file.exists () : # IF FILE EXISTS
       infile = open('accounts.data','rb') # OPENS THE FILE IN BINARY FORMAT
       mylist = pickle.load(infile) # SERIALIZED DATA IN FILE LOADED TO MYLIST
       for item in mylist :
           if item.accNo == num :
               cid = item.cif_id
       for item in mylist :
           if item.cif_id == cid :
               print()
               print(f"ACCOUNT NO: {item.accNo}  ACCOUNT NAME: {item.name} ACC TYPE:{item.acc_type}  ACCOUNT BALANCE: {item.deposit}")
               if item.acc_type == "deposit":
                   print(f"INTEREST RATE: {item.interest_rate}  PERIOD: {item.period} MATURITY AMOUNT: {item.maturity_amount} MATURITY DATE:{item.maturity_date}")
       infile.close() # CLOSES THE FILE
   else :
       print("No records to display")

# TO CLOSE A DEPOSIT ACCOUNT AND TRANSFER PROCEEDS WITH INTEREST TILL DATE TO SAVINGS ACCOUNT
def deleteAccount(num) :
    file = pathlib.Path("accounts.data")
    if file.exists () :
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        flag = 0
        for item in oldlist:
            if (int(item.accNo) == int(num)) :
                flag = 1
                if item.acc_type == "deposit":
                    cifid = item.cif_id 
                    for item in oldlist:
                        if (int(item.cif_id) == int(cifid)) and item.acc_type == 'savings' :
                            sbacc = item.accNo
                    for item in oldlist :
                        if (int(item.accNo) == int(num)) :
                            today = datetime.date.today()
                            diff = (today - item.open_date).days # converted difference in dates to integer for calculation
                            t = diff/365
                            r = item.interest_rate /100
                            if item.int_type == 'simple':
                                closure_amount = item.deposit*(1+(r*t)) 
                                
                            if item.int_type == 'compound':
                                closure_amount = item.deposit*math.pow((1+r),t)                
                    for item in oldlist:
                        if (int(item.accNo) == int(sbacc)):
                                item.deposit += closure_amount
                                print(f"Your account {num} has been closed successfully. Your {item.accNo} balance is {item.deposit}")
                    for item in oldlist:
                        if (int(item.accNo) != int(num)) :
                            newlist.append(item)
                    
                else:
                        print("Contact branch for closure")
                        for item in oldlist:
                            newlist.append(item)
                        
        if flag == 0 :
                print("Invalid deposit number!!")
                for item in oldlist:
                    newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')  
  
#  MODIFY CUSTOMER DETAILS
def modifyAccount(num):
       file = pathlib.Path("accounts.data")
       if file.exists ():
           infile = open('accounts.data','rb')
           oldlist = pickle.load(infile)
           infile.close()
           os.remove('accounts.data')
           for item in oldlist :
               if item.accNo == num :
                   print(f"Enter details you wish to modify in your Account Number : {item.accNo}")
                   print("Enter number of the details to be modified(Ex: enter 3 if phone number to be changed)")
                   print("1.Name 2.Address 3.Phone number 4.Email id ")
                   select = input()
                   if select == '1':
                       item.name = input("Account Holder Name to be modified as : ")
                   elif select == '2':
                       item.address = input("Account holder's address to be modified as : ")
                   elif select == '3':
                       item.phone_no = input("Enter new phone number : ")
                   elif select == '4':
                       item.email_id = input("Enter new email id :")
                   else :
                       print("Invalid selection")                         
           outfile = open('newaccounts.data','wb')
           pickle.dump(oldlist, outfile)
           outfile.close()
           os.rename('newaccounts.data', 'accounts.data')
           print("Modified successfully")

# TO CHANGE PASSWORD
def password_change(num) :  
   file = pathlib.Path("accounts.data")
   if file.exists ():
       infile = open('accounts.data','rb')
       oldlist = pickle.load(infile)
       infile.close()
       os.remove('accounts.data')
       for item in oldlist :
               if item.accNo == num :
                    in_pwd = input("Enter your password: ")
                    if in_pwd == item.password:
                           item.password = new_password_new_user()   
                           print("Password changed successfully")
                    else :
                        print("Wrong password entered!!! Retry")
       outfile = open('newaccounts.data','wb')
       pickle.dump(oldlist, outfile)
       outfile.close()
       os.rename('newaccounts.data', 'accounts.data')

# function to check if sign in password correct
def pwd_checker(num) :
    flag = 0
    file = pathlib.Path("accounts.data")
    if file.exists() :
       infile = open('accounts.data','rb')
       oldlist = pickle.load(infile)
       infile.close()
       for item in oldlist :
               if item.accNo == num :
                    in_pwd = input("Enter your password: ")
                    if in_pwd == item.password:
                            flag = 1  
                    else :
                        print("Wrong password entered!!! Retry")
       return flag
'''
# ADMIN PURPOSE - TO TEST THE PROGRAM
def list_all_account() :
               
   file = pathlib.Path("accounts.data")
   if file.exists() :
       infile = open('accounts.data','rb')
       mylist = pickle.load(infile)
       infile.close()
       
       for item in mylist :
           if item.acc_type == "savings":
               print(f"Customer id   {item.cif_id}   AccountNo  {item.accNo}  Name  {item.name} Balance  {item.deposit}  Type {item.acc_type}")
               print(f"Dob   {item.dob}  Address {item.address} Email id {item.email_id} Phone number {item.phone_no}")
           if item.acc_type == "deposit":
               print(f"Customer id   {item.cif_id}  AccountNo  {item.accNo}  Name  {item.name} Balance  {item.deposit} Type {item.acc_type}")
               print(f"Interest type: {item.int_type} interest_rate {item.interest_rate} Maturity_amount {item.maturity_amount} Period {item.period}")
   else :
       print("No records to Search")
'''

# TO CHECK IF PARTICULAR ACCOUNT EXISTS IN DATA FILE   
def check_if_account_exists(num) :
    file = pathlib.Path("accounts.data")
    if file.exists ():
       infile = open('accounts.data','rb')
       mylist = pickle.load(infile)
       infile.close()
       flag = 0
       for item in mylist :
          if (int(item.accNo) == int(num)) :
                   flag = 1
                  
       return flag

#--------------------------------------------------------------------------------------
# main program----------------------------------------------------------------

selection = intro()
if selection == '1':
    num = int(input("Enter your account no: "))
    pwd_check = pwd_checker(num)
    if pwd_check == 1:
        display_menu(num)
    else:
        print("Invalid credentials!!! Retry")
     
elif selection == '2':
    signup()
    print("Thanks for opening account with us .Looking forward for a wonderful experience with us ")

#list_all_account()
