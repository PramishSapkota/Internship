class User:
    # Class variable to store all users
    
    # users_database = {
    # "alice": {"passcode": "1234", "username": "Alice","balance": 1000},
    # "bob": {"passcode": "5678","username": "Bob", "balance": 500},
    # "charlie": {"passcode": "9101","username": "Charlie","balance": 2000}
    # }

    users_database = {}

    def __init__(self, name, username, password, balance=0):
        self.name = name
        self.username = username
        self.__password = password
        self.__balance = balance
        # Add this user to the class database
        User.users_database[username] = self

    # password validation
    def check_password(self, password):
        return self.__password == password

    # getter
    def get_balance(self):
        return self.__balance

    # setter
    def set_balance(self, amount):
        self.__balance = amount
    
    # Class method to get user by username
    @classmethod
    def get_user(cls, username):
        return cls.users_database.get(username)
    
    # Class method to check if username exists
    @classmethod
    def username_exists(cls, username):
        return username in cls.users_database

    def __repr__(self):
        return f'Username={self.name}, username={self.username}, balance={self.get_balance()})'
    
    # def __str__(self):
    #     users = []
    #     for i in User.users_database.keys():
    #         users.append(i)
            
    #     return users



class BankAccount(User):
    
    def __init__(self, username, password, name=None, balance=0):
        # If user exists, retrieve their data
        # existing_user = User.get_user(username)
        # if existing_user:
        #     # super().__init__(name or existing_user.name, username, password, existing_user.get_balance())
        #     super().__init__(existing_user.name, username, password, existing_user.get_balance())
        # else:
            super().__init__(name, username, password, balance)
    
    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        
        if amount <= 0:
            print("Invalid amount.")
            return
        
        new_balance = self.get_balance() + amount
        self.set_balance(new_balance)
        
        # Update in the class database
        User.users_database[self.username] = self
        
        print(f"Deposited Rs.{amount}")
        print(f"New Balance = Rs.{new_balance}")
    
    def withdraw(self):
        amount = int(input("Enter withdraw amount: "))
        
        if amount <= 0:
            print("Invalid amount.")
            return
        
        if amount > self.get_balance():
            print("Insufficient balance.")
            return
        
        new_balance = self.get_balance() - amount
        self.set_balance(new_balance)
        
        # Update in the class database
        User.users_database[self.username] = self
        
        print(f"Withdrawn Rs.{amount}")
        print(f"Remaining Balance = Rs.{new_balance}")
    
    def check_balance(self):
        print(f"Current Balance = Rs.{self.get_balance()}")


class ATMApp:
    
    def __init__(self):
        pass
    
    # signup fn    
    def signup(self):
        print("\n===== SIGNUP =====")  

        while True: 
            
            name = input("Enter name: ")
            if name == "":
                print("Name cannot be empty")
                continue

            else:
                break

        while 1:
            username = input("Enter username: ")
            if username == "":
                print("Username cannot be empty")
                continue
            
            if not User.username_exists(username):
                break      # username is unique, proceed
            print("Username already taken. Try again.")
        
        while True:
            password = input("Enter password: ")
            if password == "":
                print("Password cannot be empty")
                continue
            re = input("Re-Enter password: ")
            if password == re:
                break

            else:
                print("Passwords didnt match")
        
        balance = int(input("Enter initial deposit: "))
        account = BankAccount(username, password, name, balance)
        print("Account created successfully.")
    
    # ---------------- LOGIN ----------------
    
    def login(self):
        print("\n===== LOGIN =====")
        
        username = input("Enter username: ")
        
        # Check if username exists using User class method
        if not User.username_exists(username):
            print("Username does not exist.")
            return
        
        user = User.get_user(username)
        
        tries = 3
        
        while tries > 0:
            password = input("Enter password: ")
            
            if user.check_password(password):
                print(f"\nWelcome {user.name}!")
                
                # Create BankAccount object from existing user
                account = BankAccount(username, password)
                
                self.menu(account)
                return
            else:
                tries -= 1
                print(f"Wrong password :( {tries}attempt(s) left")
        
        print("All attempts exhausted.")
    
    
    # MENU fn
    def menu(self, account):
        while True:
            print("\n====== MENU ======")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")
            print("5. Exit")
            
            choice = input("Enter choice: ")
            
            match choice:
                case "1":
                    account.check_balance()
                case "2":
                    account.deposit()
                case "3":
                    account.withdraw()
                case "4":
                    print("Logging out...")
                    break
                case "5":
                    print("Exiting...")
                    exit()
                case _:
                    print("Invalid choice.")
    
   
    
    def run(self):
        while True:
            print("\n======= ATM =======")
            print("1. Signup")
            print("2. Login")
            print("3.Print Dictionary")
            print("4. Exit")
            
            choice = input("Enter choice: ")
            
            match choice:
                case "1":
                    self.signup()

                case "2":
                    self.login()

                case "3":
                    print("Database So Far")
                    print(User.users_database)
                    # print(User)
                    # its displaying empty dictionary
                    # print(self.__dict__) # {}
                    #bcz the ATMApp class has no attributes



                case "4":
                    print("Exiting...")
                    break
                
                case _:
                    print("Invalid choice.")

# Seed initial users
BankAccount("alice", "1234", "Alice", 1000)
BankAccount("bob", "5678", "Bob", 500)
BankAccount("charlie", "9101", "Charlie", 2000)

app = ATMApp()
app.run()
