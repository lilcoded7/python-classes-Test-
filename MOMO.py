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

# importing sqlite3
import sqlite3
# connecting to database
con = sqlite3.connect('network.db')
# create cursor
cur = con.cursor()     


# creating a table for database 
try:
    cur.execute("""CREATE TABLE mtn(username text, password text, email text, contact text)""")
    cur.execute("""CREATE TABLE vodafone(username text, password text, email text, contact text)""") 
except:
    pass 



# parent class 
class Bank():
    
    def __init__(self):
        self.wallet = 0

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if self.wallet < amount:
            print('Insufficient Balance')
        else:
            self.wallet -= amount
        print(f'withdraw : {amount} current balance is {self.wallet}')

    def transfer(self, other, amount_out):
        self.withdraw(amount_out)
        
        

    def Balance(self):
        print(f'Dear Customer your current account balance is {self.wallet}')
 
    

# b = Bank()
# b.deposite(50)
# b.withdraw(10)
# b.Balance()
# b.sendmoney(10, 30)

# MTN CUSTOMER CLASS 
class MTN_Network(Bank):

    def __init__(self):
        self.username          = self.username
        self.password          = self.password
        self.email             = self.email
        
        
        # MTN USER REGISTERATION METHOD
    def Register(self):
        print('=============MTN Registeration===============')
        print('                                            ')
        self.username = input('Enter username : ')
        self.password = input('Enter password : ')
        self.email    = input('Enter email : ')
        self.conntact = self.MTN_Number()
        
        # saving customers datails to the database
        saveMTN       = self.save_user()
        
        # printing out customers details
        print('                                                                  ')
        print('-----------------Confirm Registeration Details--------------------')
        print(f'username        : {self.username}')
        print(f'password        : {self.password}')
        print(f'email           : {self.email}')
        print('                                                                  ') 
        print('press 1.Confirm   2.Go back') 
        customerInput = input('> ')
        if customerInput == '1':
            pass 
        else:
            return self.Register()
        

    def showDetails(self):
        print(self.username)

    # saving MTN user to database
    def save_user(self):
        userInfo = (self.username, self.password, self.email, self.conntact)
        sql      = '''INSERT INTO mtn(username, password, email, contact) values(?,?,?,?)'''
        cur.execute(sql, userInfo)
        # commiting to database
        con.commit

        # MTN USER AUTHENTICATION METHOD
    def auth(self):
        print('---------------------mtn auth-----------------------')
        users = cur.execute('SELECT * FROM mtn')
        print('---------------------mtn auth-----------------------')
        for row in users:
            print('---------------------mtn auth-----------------------')
            if row[0]==self.username and row[1]==self.password:
                print('login successful')
                return True
            return False

        # MTN USER LOGIN METHOD
    def login(self):
        self.username = input('Enter username : ')
        self.password = input('Enter password : ')
        # customer authentication 
        authenticate  = self.auth()
        if authenticate:
            print('=========login successful===========')
        else:
            print('================mtn aut fail======================================')
            print('Invalide Credentials ')


        # generating MTN customer Number 
    def MTN_Number(self):
        numCode   = '054'
        randomNum = random.randint(0000000, 9999999)
        mtnNUmber = numCode + str(randomNum)
        print('your Mtn number is : ', mtnNUmber)
        
       

        #mtn customer services
    def services(self):
        print('press  *170# .Menu')
        userInput = input('> ')
        if userInput == '*170#':
            print('press  1.Send Money')
            print('press  2.Send deposite')
            print('press  3.Send withdraw')
            print('press  4.Send check balance')
        else:
            print('Invalide Response')
            return self.services() 

            # allow cash out function 
    def allowCash(self):
            print('press  1.allow cash')
            print('press  2.return to menu')

            userinput = input('> ')
            if userinput == '1': # allowing cash out 
                print('cash is allow')
            elif userinput == '2': # returning user to main manu
                return self.services()
                

            



# vodafone parent class 
class VodafoneNetwork:

    def __init__(self):
        self.username          = ''
        self.password          = ''
        self.email             = ''
        
        
        
    # register vodafone users
    def Register(self):
        print('=============vodafone Registeration===============')
        print('                                                  ')
        self.username = input('Enter username : ')
        self.password = input('Enter password : ')
        self.email    = input('Enter email : ')
        self.conntact = self.vodafoneNumber()
        
        # saving customers datails to the database
        save       = self.save_user()
        
        # printing out customers details
        print('                                                                  ')
        print('-----------------Confirm Registration Details--------------------')
        print(f'username        : {self.username}')
        print(f'password        : {self.password}')
        print(f'email           : {self.email}')
        print('                                                                  ') 
        print('press 1.Confirm   2.Go back') 
        customerInput = input('> ')
        if customerInput == '1':
            pass 
        else:
            return self.Register()

    # saving vodafone customers to database
    def save_user(self):
        print('--------------------------------------------------------------------------------------------')
        userInfo = (self.username, self.password, self.email, self.conntact)
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
            if row[0]==self.username and row[1]==self.password:
                print('login successful')
                return True
            return False

    # generating vodafone number
    def vodafoneNumber(self):
        numCode   = '050'
        randomNum = random.randint(0000000, 9999999)
        vodafoneNUmber = numCode + str(randomNum)
        print('your vodafone number is : ', vodafoneNUmber)

    def showDetails(self):
        print(self.username)
       
        # vodafone login method
    def login(self):
        self.username = input('Enter username : ')
        self.password = input('Enter password : ')
        # customer authentication 
        authenticate  = self.auth()
        if authenticate:
            print('=========login successful===========')
        else:
            print('================voda aut fail======================================')
            print('Invalide Credentials ')

        # vodafone customer service 
    def services(self):
        print('press  *110# .Menu')
        userInput = input('> ')
        if userInput == '*170#':
            print('press  1.Send Money')
            print('press  2.Send deposite')
            print('press  3.Send withdraw')
            print('press  4.Send check balance')
        else:
            print('Invalide Response')
            return self.services() 







# main function 
def main():
    print('===============HELLO WELCOME TO CODED NETWORKING=================')
    print('                                                              ')
    print(' press  1.Register As vodafone user      2.Register As MTN user')

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

        # directing user to MTN registeration
    elif userInput == '2':
        MTN = MTN_Network()
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








        


    


        