class BankAccount:

    def __init__(self, username, passcode, balance):
        self.username = username
        self.__passcode = passcode
        self.balance = balance

    def authenticate(self):

        tries = 3

        while tries > 0:

            password = input("Enter password: ")

            if password == self.__passcode:
                print(f"\nWelcome {self.username}!")
                return True

            else:
                tries -= 1
                print(f"Wrong password :( \n---{tries} attempt(s) left---")

        print("All attempts exhausted.")
        return False

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self):

        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            self.balance += amount
            print(f"New Balance: {self.balance}")

        else:
            print("Invalid amount.")

    def withdraw(self):

        amount = int(input("Enter withdraw amount: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount <= self.balance:
            self.balance -= amount
            print(f"New Balance: {self.balance}")

        else:
            print("Insufficient balance.")


class ATM:

    def __init__(self):

        self.users = {
            "alice": BankAccount("alice", "1234", 1000),
            "bob": BankAccount("bob", "5678", 500),
            "charlie": BankAccount("charlie", "9101", 2000)
        }

    def login(self):

        while True:

            username = input("\nEnter username: ")

            if username not in self.users:
                print("Username does not exist.")
                continue

            user = self.users[username]

            if user.authenticate():
                self.menu(user)

            else:
                print("Exiting...")
                break

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
                    user.check_balance()

                case "2":
                    user.deposit()

                case "3":
                    user.withdraw()

                case "4":
                    print("Logging out...")
                    break

                case "5":
                    print("Exiting program...")
                    exit()

                case _:
                    print("Invalid choice.")


# Driver Code
atm = ATM()
atm.login()