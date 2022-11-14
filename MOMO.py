# PYTHON ASSIGNMENT 
# ======================
# Using SQLITE3/MongoDB as your Database. Build a MOMO system console clone with python only(No framework)

# ENTITIES
# 1. User
# 2. Momo Network(eg: MTN, VODAFONE)
# 3. Could add extra entities

# FEATURES
# 1. User auth (Login & Signup)
# 2. User Transactions
#  - Deposit
#  - Withdrawal
# 3. Implement the AGENT and USER "Allow Cashout" flow for withdrawal

# importing random
import random

# importing time and date 
from datetime import datetime

# importing sqlite3
import sqlite3
# connecting to database
con = sqlite3.connect('network.db')
# create cursor
cur = con.cursor()     


# CREATING DATABASE TABLE FOR VARIOUS NETWORK (MTN AND VODAFONE)
try:
    cur.execute("""CREATE TABLE mtn(username text, password text, email text, contact text, history text)""")
    cur.execute("""CREATE TABLE vodafone(username text, password text, email text, contact text, history text)""")
except:
    pass 



#     TRANSACTION CLASS FUNCTION(PARENT CLASS) 
class Transaction():
    
    def __init__(self):
        self.wallet = float(0)
        
    
    #   DEPOSIT METHOD  
    def deposit(self, amount):
        self.wallet += amount 
        print(f'Your Account has been credited with {amount} current Balance is {self.wallet}')

        timedate =  datetime.now()
        self.transactionhistory = f'Deposit -{amount}-{timedate} Balance {self.wallet} '
    
    #   WITHDRAW METHOD
    def withdraw(self, amount):
        if self.wallet < float(amount): # checking wallet before withdrawal 
            print('Insufficient Balance')
        else:
            self.wallet -= float(amount)
            print(f'withdraw : {amount} current balance is {self.wallet}')
            # time and date
            timedate =  datetime.now()
            self.transactionhistory = f'Withdraw -{amount}-{timedate} Balance {self.wallet} '

    #   MONEY TRANSFER METHOD 
    def transfer(self, receiverNumber, amount_out):
        self.withdraw(amount_out)
        receiverNumber.deposit()
    
    #   BUY AIRTIME METHOD 
    def buyAirtime(self, amount):
        #  checking wallet before customer buy's airtime
        if self.wallet < float(amount): 
            print('Insufficient Balance')
        else:
            self.wallet -= float(amount)
            print(f'withdraw : {amount} current balance is {self.wallet}')
            # time and date 
            timedate =  datetime.now()
            self.transactionhistory = f'Withdraw -{amount}-{timedate} Balance {self.wallet} '

        
    #   CHECK BALANCE METHOD 
    def Balance(self):
        print(f'Dear Customer your current account balance is {self.wallet}')
 
    



# MTN CLASS FUNCTION (CHILD CLASS)
class MtnNetwork(Transaction):

   
    # MTN USER/CUSTOMER REGISTERATION
    def register(self):
        print('=============MTN User Registeration===============')
        print('                                                  ')
        self.mtnusername = input('Enter username : ')
        self.mtnpassword = input('Enter password : ')
        self.mtnemail    = input('Enter email : ')
               
        
        # printing out customers details
        print('                                                                  ')
        print('-----------------Confirm Registration Details--------------------')
        print(f'username        : {self.mtnusername}')
        print(f'password        : {self.mtnpassword}')
        print(f'email           : {self.mtnemail}')
        print('                                                                  ') 
        self.mtnconntact = self.mtnNumber()
        self.pin                =  '4501'
        print(f'Your MTN Pin Number is {self.pin}')

         # saving customers datails to the database
        save       = self.save_user()

         # confirming user's Register details
        print('press 1.Confirm   2.Go back') 
        customerInput = input('> ')
        if customerInput == '1': 
            pass 
        else:
            return self.Remtn

    # SAVING USER'S REGISTERATION DETAILS TO DATABASE 
    def save_user(self):
        print('--------------------------------------------------------------------------------------------')
        userInfo = (self.mtnusername, self.mtnpassword, self.mtnemail,  self.mtnconntact)
        sql      = '''INSERT INTO mtn(username, password, email, contact) values(?,?,?,?)'''
        cur.execute(sql, userInfo)
        # commiting to database
        con.commit
    
    # MTN USER AUTHENTICATION
    def auth(self):
        print('---------------------MTN auth-----------------------')
        users = cur.execute('SELECT * FROM mtn')
        print('---------------------MTN auth-----------------------')
        for row in users:
            print('---------------------MTN auth-----------------------')
            if row[0]==self.mtnusername and row[1]==self.mtnpassword:
                print('login successful')
                return True
            return False

    # GENETATING RAMDOM NUMBER TO USER'S/CUSTOMERS
    def mtnNumber(self):
        numCode   = '054'
        randomNum = random.randint(0000000, 9999999)
        mtnNumber = numCode + str(randomNum)
        print('your MTN number  : ', mtnNumber) # printing out MTN user numbers

    
       
        # MTN USER LOGIN 
    def login(self):
        self.mtnusername = input('Enter username : ')
        self.mtnpassword = input('Enter password : ')
        # customer authentication 
        authenticate  = self.auth()
        if authenticate:
            print('=========login successful===========')
            return self.mtnservices()
        else:
            print('================MTN aut fail======================================')
            print('Invalide Credentials ')
            return self.register()

        # MTN USER CUSTOMER SERVICES
    def mtnservices(self):
        print('press  *110# .Menu   0.Exit')
        userInput = input('> ')
        if userInput == '*110#':
            # customer offers
            print('press  1.Send Money')
            print('press  2.Deposite  Cash')
            print('press  3.Withdraw  Cash')
            print('press  4.Check Account Balance')
            print('press  5.Buy Airtime')

            
            customerInput = input('> ') # taking user/customer input 
                
            # directing user/customers to MTN available offers 
            if customerInput == '1': 
                return self.mtnAgent()  # calling agent class method

            elif customerInput == '2': # returning user/customer to deposit function
                    amount = float(input('Enter amount : '))
                    self.deposit(amount)
                    return self.mtnservices()

                    # returning user to withdraw
            elif customerInput == '3':
                amount = float(input('Enter amount : '))
                self.withdraw(amount) # calling withdraw class methode form parent class (Transactions)
                return self.mtnservices()

                # directing user/customer to check account balance 
            elif customerInput == '4':
                self.Balance() # calling Balance class methode form parent class (Transactions)
                return self.mtnservices()

                # directing user/customer to check account airtime
            elif customerInput == '5':
                amount = float(input('Enter amount: '))
                self.buyAirtime(amount) # calling buy airtime class method
                return self.mtnservices() # returning user/customer to mtn services

            else:
                print('-------------------Invalide Response--------------------')
                return self.mtnservices() # returning user/ customer back to services 

            # returning user to login function
        elif userInput == '0':
            return self.login()

        else:
            print('Invalide Credentials')
            return self.mtnservices() # returning user/ customer back to services


    # MTN MONEY TRANSFER METHOD (POLYMORPHISM)
    def transfer(self, amount_out):
        if self.wallet < amount_out:
            print('--------------------Insufficient Balance------------------------')
        else: 
            self.wallet -= amount_out 
            print(f'you have successfully transfer {amount_out} the number {self.reciverNumber}')
            timedate =  datetime.now()
            self.transactionhistory = f'Sent Money -{amount_out}-{timedate} Balance {self.wallet} '


    # ALLOW CASH OUT FUNCTION 
    def allowCash(self):
            print('press  1.allow cash')
            print('press  2.return to menu')

            #customer money transfer 
            userinput = input('> ')
            if userinput == '1': # allowing cash out 
                print('cash is allow')
                return self.mtnAgent()  # returning mtn agent function 
            else:
                print('---------------------Invalid Credentials----------------------')
                return self.allowCash()

    
    #  MTN AGENT
    def mtnAgent(self):
        print('--------Agent Only-------')
        print('                          ')
        print('--------Enter Agent Code-------')
        _agentInput = input("> ")
        __agenCode = '*175#'
        
        # agent secrete pin authentication 
        if _agentInput ==__agenCode:
            print('Enter customer number')
            customerNum = input('> ')

            # calling customer' function
            return self.customer()
        else:
            print('Incorrect pin')
            return self.mtnAgent()


    # MTN CUSTOMER/USER METHOD
    def customer(self):
        print('-------------Customer Only----------------')
        print('                                           ')
        amount     = float(input('Enter amount : '))
        self.reciverNumber = int(input("Enter receiver's number : "))
        _pin       = input('Enter pin code : ')

            # mtn money transfer
        if _pin    == self.pin:
            if self.wallet < amount:
                print('Insufficient Balance')
            else:
                self.transfer(amount)
                self.Balance()
                return self.mtnservices()
        print('===================================================================') 
        return self.customer() 







#    VODAFONE CLASS FUNCTION(CHILD CLASS)
class VodafoneNetwork(Transaction):

   
    #   VODAFONE USER REGISTERATION 
    def register(self):
        print('=============vodafone Registeration===============')
        print('                                                  ')
        self.vodafoneusername = input('Enter username : ')
        self.vodafonepassword = input('Enter password : ')
        self.vodafoneemail    = input('Enter email : ')
               
        
        # printing out customers details
        print('                                                                  ')
        print('-----------------Confirm Registration Details--------------------')
        print(f'username        : {self.vodafoneusername}')
        print(f'password        : {self.vodafonepassword}')
        print(f'email           : {self.vodafoneemail}')
        print('                                                                  ') 
        self.vodafoneconntact = self.vodafoneNumber()
        self.pin                =  '4501'
        print(f'Your vodafone Pin Number is {self.pin}')


        # saving customers datails to the database
        save       = self.save_user()


        # confirming user's Register details    
        print('press 1.Confirm   2.Go back')  
        customerInput = input('> ')
        if customerInput == '1':
            pass 
        else:
            return self.register()


    #   SAVING ALL VODAFONE USERS TO DATABASE
    def save_user(self):
        print('--------------------------------------------------------------------------------------------')
        userInfo = (self.vodafoneusername, self.vodafonepassword, self.vodafoneemail,  self.vodafoneconntact)
        sql      = '''INSERT INTO vodafone(username, password, email, contact) values(?,?,?,?)'''
        cur.execute(sql, userInfo)
        # commiting to database
        con.commit
    
    #   VODAFONE USER/CUSTOMER AUTHENTICATION
    def auth(self):
        print('---------------------voda auth-----------------------')
        users = cur.execute('SELECT * FROM vodafone')
        print('---------------------voda auth-----------------------')
        for row in users:
            print('---------------------voda auth-----------------------')
            if row[0]==self.vodafoneusername and row[1]==self.vodafonepassword:
                print('login successful')
                return True
            return False

    #   GENERATING RANDOM VODAFONE USER'S NUMBER
    def vodafoneNumber(self):
        numCode   = '050'
        randomNum = random.randint(0000000, 9999999)
        vodafoneNUmber = numCode + str(randomNum)
        print('your vodafone number is : ', vodafoneNUmber)

    
       
    #   VODAFONE LOGIN METHOD
    def login(self):
        self.vodafoneusername = input('Enter username : ')
        self.vodafonepassword = input('Enter password : ')
        # customer authentication 
        authenticate  = self.auth()
        if authenticate:
            print('=========login successful===========')
            return self.vodafoneservices()
        else:
            print('================voda aut fail======================================')
            print('Invalide Credentials ')

    #   VODAFONE CUSTOMER SERVICES 
    def vodafoneservices(self):
        print('press  *110# .Menu   0.Exit')
        userInput = input('> ')
        if userInput == '*110#':
         #  available offers for customers/users
            print('press  1.Send Money')
            print('press  2.Deposite  Cash')
            print('press  3.Withdraw  Cash')
            print('press  4.Check Account Balance  Cash')
            print('press  5.Buy Airtime')

            
            customerInput = input('> ') # taking user/customer input 
                
            # directing user/customers to MTN available offers 
            if customerInput == '1':  # directing user to send money
                return self.vodafoneAgent()

            elif customerInput == '2': # returning user/customer to deposit function
                    amount = float(input('Enter amount : '))
                    self.deposit(amount)
                    return self.vodafoneservices()

            #    returning user to withdraw
            elif customerInput == '3':
                amount = float(input('Enter amount : '))
                self.withdraw(amount)
                return self.vodafoneservices()

            #    directing user/customer to check account balance 
            elif customerInput == '4':
                self.Balance()
                return self.vodafoneservices()

            #    directing user/customer to check account balance 
            elif customerInput == '5':
                amount = float(input('Enter amount: '))
                self.buyAirtime(amount)
                return self.vodafoneservices()

            else:
                print('-------------------Invalide Response--------------------')
                return self.vodafoneservices() # returning user/ customer back to services 

        #    returning user to login function
        elif userInput == '0':
            return self.login()

        else:
            print('Invalide Credentials')
            return self.vodafoneservices() # returning user/ customer back to services


    #   VODAFONE MONEY TRANSFER (POLYMORPHISM)
    def transfer(self, amount_out):
        if self.wallet < amount_out:
            print('--------------------Insufficient Balance------------------------')
        else: 
            self.wallet -= amount_out 
            print(f'you have successfully transfer {amount_out} the number {self.reciverNumber}')
            timedate =  datetime.now()
            self.transactionhistory = f'Sent Money -{amount_out}-{timedate} Balance {self.wallet} '


    #   VODAFONE AGENT
    def vodafoneAgent(self):
        print('--------Agent Only-------')
        
        self.__agentillNumber = '43003'
        print(f'Agent Til Number : {self.__agentillNumber}')
        print('                                        ')
        return self.customer()
        

    # CUSTOMER/USER METHOD
    def customer(self):
        print('-------------Customer Only----------------')
        print('                                           ')
        
        tillNumber = input('Enter Agent Till Number : ')

        if tillNumber == self.__agentillNumber:
            print(  "Enter Receiver's Number : ")
            self.reciverNumber = input('> ')
            amount = float(input('Enter Amount : '))
            self.transfer(amount)
            self.Balance()
            return self.vodafoneservices()
        else:
            return self.customer()


# MAIN FUNCTION
def main():
    print('===============HELLO WELCOME TO TROPITEQ MOBILE BANKING=================')
    print('                                                              ')
    print(' press  1.Register As Vodafone User      2.Register As MTN User')
    print('                                                               ')
    print('press   3.login Vodafone User            4.login As MTN User')

    # taking user to vodafone registeration 
    userInput = input('> ')  # taking user's input 
    if userInput == '1':
        vodafone = VodafoneNetwork()
        vodafone.register() # calLinging vadafone function 

        # directing user to vodafone login
        print('press  1.Login')
        user_input = input('> ')
        if user_input == '1':
            vodafone.login()
        else:
            print('--------------- Invalide Credentials-----------------------')
            return main()

    #    directing user to MTN registeration
    elif userInput == '2':
        MTN = MtnNetwork()
        MTN.register() 

        # directing user to MTN login after registeration
        print('press  1.Login')
        user_Input = input('> ')
        if user_Input == '1':
            MTN.login()
        else:
            print('--------------- Invalide Credentials-----------------------')
            return main()
    
    # directing user/customer vodafone login 
    elif userInput == '3':
        vodafone = VodafoneNetwork()
        vodafone.login()
        return main()

    # directing user/customer to MTN login
    elif userInput == '4':
        MTN = MtnNetwork()
        MTN.login() 
        return main()


    else:
        print('--------------------Invalide Credentials-----------------------')
        return main()




main()








        


    


        