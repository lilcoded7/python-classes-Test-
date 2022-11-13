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


# creating a table for database 
try:
    cur.execute("""CREATE TABLE mtn(username text, password text, email text, contact text, history text)""")
    cur.execute("""CREATE TABLE vodafone(username text, password text, email text, contact text, history text)""")
except:
    pass 



# parent class 
class Transaction():
    
    def __init__(self):
        self.wallet = float(0)
    
        # DEPOSIT METHOD  
    def deposit(self, amount):
        self.wallet += amount
        print(f'Your Account has been credited with {amount} current Balance is {self.wallet}')

        timedate =  datetime.now()
        self.transactionhistory = f'Deposit -{amount}-{timedate} Balance {self.wallet} '
    
        # withdraw method
    def withdraw(self, amount):
        if self.wallet < float(amount):
            print('Insufficient Balance')
        else:
            self.wallet -= float(amount)
            print(f'withdraw : {amount} current balance is {self.wallet}')

            timedate =  datetime.now()
            self.transactionhistory = f'Withdraw -{amount}-{timedate} Balance {self.wallet} '

        # tansfer money 
    # def transfer(self, receiverNumber, amount_out):
    #     self.withdraw(amount_out)
    #     receiverNumber.deposit()
        
        
        #  check blance 
    def Balance(self):
        print(f'Dear Customer your current account balance is {self.wallet}')
 
    

# T = Transaction()
# T.deposite(50)
# T.withdraw(10)
# T.Balance()
# T.sendmoney(10, 30)

# MTN CUSTOMER CLASS 
class mtnNetwork(Transaction):

   
    # register mtn users
    def Register(self):
        print('=============mtn Registeration===============')
        print('                                                  ')
        self.mtnusername = input('Enter username : ')
        self.mtnpassword = input('Enter password : ')
        self.mtnemail    = input('Enter email : ')
        
        
        # saving customers datails to the database
        
        
        # printing out customers details
        print('                                                                  ')
        print('-----------------Confirm Registration Details--------------------')
        print(f'username        : {self.mtnusername}')
        print(f'password        : {self.mtnpassword}')
        print(f'email           : {self.mtnemail}')
        print('                                                                  ') 
        self.mtnconntact = self.mtnNumber()
        self.pin                =  '4501'
        print(f'Your vodafone Pin Number is {self.pin}')


        save       = self.save_user()

            # confirming user's Register details 
        print('press 1.Confirm   2.Go back') 
        customerInput = input('> ')
        if customerInput == '1':
            pass 
        else:
            return self.Register()

    # saving mtn customers to database
    def save_user(self):
        print('--------------------------------------------------------------------------------------------')
        userInfo = (self.mtnusername, self.mtnpassword, self.mtnemail, self.mtnconntact)
        sql      = '''INSERT INTO vodafone(username, password, email, contact) values(?,?,?,?)'''
        cur.execute(sql, userInfo)
        # commiting to database
        con.commit
    
    # mtn users authentication
    def auth(self):
        print('---------------------mtn auth-----------------------')
        users = cur.execute('SELECT * FROM vodafone')
        print('---------------------mtn auth-----------------------')
        for row in users:
            print('---------------------mtn auth-----------------------')
            if row[0]==self.mtnusername and row[1]==self.mtnpassword:
                print('login successful')
                return True
            return False

    # generating mtn number
    def mtnNumber(self):
        numCode   = '054'
        randomNum = random.randint(0000000, 9999999)
        mtnNumber = numCode + str(randomNum)
        print('your mtn number is : ', mtnNumber)

    def showDetails(self):
        print(self.vodafoneusername)
       
        # mtn login method
    def login(self):
        self.vodafoneusername = input('Enter username : ')
        self.vodafonepassword = input('Enter password : ')
        # customer authentication 
        authenticate  = self.auth()
        if authenticate:
            print('=========login successful===========')
            return self.mtnservices()
        else:
            print('================voda aut fail======================================')
            print('Invalide Credentials ')

        # mtn customer service 
    def mtnservices(self):
        print('press  *110# .Menu   0.Exit')
        userInput = input('> ')
        if userInput == '*110#':
            print('press  1.Send Money')
            print('press  2.Deposite  Cash')
            print('press  3.Withdraw  Cash')
            print('press  4.Check Account Balance  Cash')

            
            customerInput = input('> ') # taking user/customer input 
                
            # directing user/customers to MTN available offers 
            if customerInput == '1':  # directing user to send money
                return self.mtnAgent()

            elif customerInput == '2': # returning user/customer to deposit function
                    amount = float(input('Enter amount : '))
                    self.deposit(amount)
                    return self.mtnservices()

                    # returning user to withdraw
            elif customerInput == '3':
                amount = float(input('Enter amount : '))
                self.withdraw(amount)
                return self.mtnservices()

                # directing user/customer to check account balance 
            elif customerInput == '4':
                self.Balance()
                return self.mtnservices()

            else:
                print('-------------------Invalide Response--------------------')
                return self.mtnservices() # returning user/ customer back to services 

        elif userInput == '0':
            return self.login()

        else:
            print('Invalide Credentials')
            return self.mtnservices() # returning user/ customer back to services


         # mtn money transfer (Polymorphism)
    def transfer(self, amount_out):
        self.wallet -= amount_out 
        print(f'you have successfully transfer {amount_out} the number {self.reciverNumber}')
        timedate =  datetime.now()
        self.transactionhistory = f'Sent Money -{amount_out}-{timedate} Balance {self.wallet} '


      #  MTN agent
    def mtnAgent(self):
        print('--------Agent Only-------')
        print('                          ')
        print('--------Enter Agent Code-------')
        _agentInput = input("> ")
        __agenCode = '*175#'
        
        # Agent secrete pin authentication 
        if _agentInput ==__agenCode:
            print('Enter customer number')
            customerNum = input('> ')

            # calling customer' function
            return self.customer()
        else:
            print('Incorrect pin')
            return self.mtnAgent()

        

          # customer/user method
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
                return self.mtnservices()
            else:
                self.transfer(amount)
                self.Balance()
                return self.mtnservices()
        else:
            print('===================================================================') 
            return self.customer() 






# vodafone parent class 
class VodafoneNetwork(Transaction):

   
    # register vodafone users
    def Register(self):
        print('=============vodafone Registeration===============')
        print('                                                  ')
        self.vodafoneusername = input('Enter username : ')
        self.vodafonepassword = input('Enter password : ')
        self.vodafoneemail    = input('Enter email : ')
        
        
        # saving customers datails to the database
        
        
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


        save       = self.save_user()

            # confirming user's Register details 
        print('press 1.Confirm   2.Go back') 
        customerInput = input('> ')
        if customerInput == '1':
            pass 
        else:
            return self.Register()

    # saving vodafone customers to database
    def save_user(self):
        print('--------------------------------------------------------------------------------------------')
        userInfo = (self.vodafoneusername, self.vodafonepassword, self.vodafoneemail, self.vodafoneconntact)
        sql      = '''INSERT INTO vodafone(username, password, email, contact) values(?,?,?,?)'''
        cur.execute(sql, userInfo)
        # commiting to database
        con.commit
    
    # vodafone users authentication
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

    # generating vodafone number
    def vodafoneNumber(self):
        numCode   = '050'
        randomNum = random.randint(0000000, 9999999)
        vodafoneNUmber = numCode + str(randomNum)
        print('your vodafone number is : ', vodafoneNUmber)

    
       
        # vodafone login method
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

        # vodafone customer service 
    def vodafoneservices(self):
        print('press  *110# .Menu   0.Exit')
        userInput = input('> ')
        if userInput == '*110#':
            print('press  1.Send Money')
            print('press  2.Deposite  Cash')
            print('press  3.Withdraw  Cash')
            print('press  4.Check Account Balance  Cash')

            
            customerInput = input('> ') # taking user/customer input 
                
            # directing user/customers to MTN available offers 
            if customerInput == '1':  # directing user to send money
                return self.vodafoneAgent()

            elif customerInput == '2': # returning user/customer to deposit function
                    amount = float(input('Enter amount : '))
                    self.deposit(amount)
                    return self.vodafoneservices()

                    # returning user to withdraw
            elif customerInput == '3':
                amount = float(input('Enter amount : '))
                self.withdraw(amount)
                return self.vodafoneservices()

                # directing user/customer to check account balance 
            elif customerInput == '4':
                self.Balance()
                return self.vodafoneservices()

            else:
                print('-------------------Invalide Response--------------------')
                return self.vodafoneservices() # returning user/ customer back to services 

        elif userInput == '0':
            return self.login()

        else:
            print('Invalide Credentials')
            return self.vodafoneservices() # returning user/ customer back to services


        # vodafone money transfer (Polymorphism)
    def transfer(self, amount_out):
        if self.wallet < amount_out:
            print('--------------------Insufficient Balance------------------------')
        else: 
            self.wallet -= amount_out 
            print(f'you have successfully transfer {amount_out} the number {self.reciverNumber}')
            timedate =  datetime.now()
            self.transactionhistory = f'Sent Money -{amount_out}-{timedate} Balance {self.wallet} '


     #  vodafone agent
    def vodafoneAgent(self):
        print('--------Agent Only-------')
        
        self.__agentillNumber = '43003'
        print(f'Agent Til Number : {self.__agentillNumber}')
        print('                                        ')
        return self.customer()
        

       # customer/user method
    def customer(self):
        print('-------------Customer Only----------------')
        print('                                           ')
        
        tillNumber = input('Enter Agent Till Number : ')

        if tillNumber == self.__agentillNumber:
            print(  "Enter Receiver's Number : ")
            self.reciverNumber = input('> ')
            amount = float(input('Enter Amount : '))
            self.transfer(amount)
            return self.vodafoneservices()
        else:
            return self.customer()


            

        
        
    
    
        






# main function 
def main():
    print('===============HELLO WELCOME TO TROPITEQ MOBILE BANKING=================')
    print('                                                              ')
    print(' press  1.Register As Vodafone User      2.Register As MTN User')

    # taking user to vodafone registeration 
    userInput = input('> ')  # taking user's input 
    if userInput == '1':
        vodafone = VodafoneNetwork()
        vodafone.Register() # calinging vadafone function 

        # directing user to vodafone login
        print('press  1.Login')
        user_input = input('> ')
        if user_input == '1':
            vodafone.login()
        else:
            print('--------------- Invalide Credentials-----------------------')
            return main()

        # directing user to MTN registeration
    elif userInput == '2':
        MTN = mtnNetwork()
        MTN.Register() 

        # directing user to MTN login after registeration
        print('press  1.Login')
        user_Input = input('> ')
        if user_Input == '1':
            MTN.login()
        else:
            print('--------------- Invalide Credentials-----------------------')
            return main()
    else:
        print('--------------------Invalide Credentials-----------------------')
        return main()




main()








        


    


        