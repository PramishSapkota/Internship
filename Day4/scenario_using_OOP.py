class BankAccount:
    def __init__(self, username, password, amount):
        self.username = username
        self.__password = password
        self.__amount = amount

    def checkpassword(self, passcode):
        return(self.__password == passcode)
    
    def getamount(self):
        return(self.__amount)
    
    def setamount(self, newamount):
        self.__amount = newamount
        print(f"New Balance: {self.getamount()}")

    def __add__(self, deposit_amount):
        if deposit_amount > 0:
            new_amount = self.getamount() + deposit_amount
            self.setamount(new_amount)
            
        else:
            print("Invalid amount.")

    def __sub__(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Invalid amount.")

        elif withdraw_amount <= self.getamount():
            new_amount = self.getamount() - withdraw_amount
            self.setamount(new_amount)

        else:
            print("Insufficient balance.")
  

# class BankApp(BankAccount):
    def deposit(self):
        deposit_amount = int(input("Enter deposit amount: "))
        self + deposit_amount

        # if deposit_amount > 0:
        #     new_amount = self.getamount() + deposit_amount
        #     self.setamount(new_amount)
            
        # else:
        #     print("Invalid amount.")

        

    def withdraw(self):
        withdraw_amount = int(input("Enter withdraw amount: "))
        self - withdraw_amount

        # if withdraw_amount <= 0:
        #     print("Invalid amount.")

        # elif withdraw_amount <= self.getamount():
        #     new_amount = self.getamount() - withdraw_amount
        #     self.setamount(new_amount)

        # else:
        #     print("Insufficient balance.")

        

class Usr:

    def __init__(self):

        self.users = {
            "alice": BankAccount("alice", "1234", 1000),
            "bob": BankAccount("bob", "5678", 500),
            "charlie": BankAccount("charlie", "9101", 2000)
        }
        '''        
        #this is how to do access password things
        # user = self.users
        #user.getpassword()
        '''


    def validateuser(self):
        while 1:
            username = input("\nEnter username: ")

            if username not in self.users:
                print("Username does not exist.")
                continue
            else:
                break
            
        tries = 3
        while tries > 0:
            password = input("\nEnter Password: ")
            user = self.users[username]
            if user.checkpassword(password):
                print(f"\nWelcome {username}!")
                break
            
            else:
                tries -= 1
                print(f"Wrong password :( \n---{tries}attempt(s) left--- ")
            
        else:
            print("All attempts exhausted.")
            print("Exiting..")
            exit()

        self.menu(user)


    def menu(self, user):

        while True:

            print("\n====== MENU ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Logout")
            print("5. Exit")

            choice = input("\nEnter choice: ")

            match choice:

                case "1":
                    print(f"Balance = {user.getamount()}")

                case "2":
                    user.deposit()

                case "3":
                    user.withdraw()

                case "4":
                    print("Logging out...")
                    self.validateuser()

                case "5":
                    print("Exiting program...")
                    exit()

                case _:
                    print("Invalid choice.")


app = Usr()
app.validateuser()

'''
O/p:

Enter username: bob

Enter Password: 5678

Welcome bob!

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 2
Enter deposit amount: 1000
New Balance: 1500

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 1
Balance = 1500

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 4
Logging out...

Enter username: alice

Enter Password: 1234

Welcome alice!

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 1
Balance = 1000

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 2
Enter deposit amount: 1000
New Balance: 2000

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 4
Logging out...

Enter username: bob

Enter Password: 5678

Welcome bob!

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 1
Balance = 1500

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit

Enter choice: 5
Exiting program...
'''

