class BankAccount:

    def __init__(self, username, passcode, balance):
        self.username = username
        self.__passcode = passcode
        self.balance = balance

    def verify_password(self, password):
        return self.__passcode == password

    def check_balance(self):
        print(f"Balance: {self.balance}")


class Bank:

    def __init__(self):

        self.users = {
            "alice": BankAccount("alice", "1234", 1000),
            "bob": BankAccount("bob", "5678", 500)
        }

    def login(self, username, password):

        user = self.users.get(username)

        if not user:
            return None

        if user.verify_password(password):
            return user

        return None


class ATM:

    def __init__(self):
        self.bank = Bank()

    def start(self):

        username = input("Username: ")
        password = input("Password: ")

        user = self.bank.login(username, password)

        if user:
            print(f"Welcome {user.username}")
            self.menu(user)

        else:
            print("Invalid credentials")

    def menu(self, user):

        while True:

            print("\n1. Balance")
            print("2. Exit")

            choice = input("Choice: ")

            match choice:

                case "1":
                    user.check_balance()

                case "2":
                    break


atm = ATM()
atm.start()