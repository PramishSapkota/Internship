import csv

FILE_NAME = "Week_2/Day6/csvs/user_record_No_OOP.csv"

fields = ["username", "password", "name", "balance"]

# Uncomment once to create file

# with open(FILE_NAME, "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(fields)
#     writer.writerow(["alice", "1234", "Alice", 1000])
#     writer.writerow(["bob", "5678", "Bob", 500])
#     writer.writerow(["charlie", "9101", "Charlie", 2000])

def get_list_of_dictionaries():
    rows = []
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)
    return rows

def update_file(list_of_dictionaries:list):
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(list_of_dictionaries)

def user_exist(username):
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["username"] == username:
                return True

    return False

def get_name(username):
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["username"] == username:
                return row["name"]
    return None

# ---------------- CHECK PASSWORD ----------------
def checkpassword(username, password):
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["username"] == username and row["password"] == password:
                return True

    return False


def add_user():

    while True:

        new_username = input("Enter username: ")
        if new_username == "":
            print("Username cannot be empty")
            continue

        if user_exist(new_username):
            print("Username already exists.")
            continue
        else:
            break

    while 1:

        password = input("Enter password: ")
        if password == "":
            print("Password cannot be empty")
            continue

        re_password = input("Re-enter password: ")

        if password != re_password:
            print("Passwords didn't match.")
            continue
        else:
            break

    while 1:
        try:
            balance = int(input("Enter initial deposit amount: "))

            if balance < 0:
                print("Balance cannot be negative.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue
        break

    while 1:
        name = input("Enter your name: ")
        if name == "":
            print("Name cannot be empty")
            continue
        else:
            break

    with open(FILE_NAME, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writerow({
            "username": new_username,
            "password": password,
            "name": name,
            "balance": balance
        })

    print("Account created successfully!")


# ---------------- CHECK BALANCE ----------------
def check_balance(username):

    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["username"] == username:
                print(f"Current Balance: {row['balance']}")
                return


# ---------------- DEPOSIT ----------------
def deposit(username):

    rows = get_list_of_dictionaries()

    for row in rows:

        if row["username"] == username:

            while True:

                try:
                    amount = int(input("Enter deposit amount: "))

                    if amount <= 0:
                        print("Amount must be positive.")
                        continue

                    row["balance"] = str(int(row["balance"]) + amount)

                    print(f"New Balance: {row['balance']}")
                    break

                except ValueError:
                    print("Please enter a valid number.")

    
    update_file(rows)


# ---------------- WITHDRAW ----------------
def withdraw(username):

    rows = get_list_of_dictionaries()

    for row in rows:

        if row["username"] == username:

            while True:

                try:
                    amount = int(input("Enter withdraw amount: "))

                    if amount <= 0:
                        print("Amount must be positive.")
                        continue

                    current_balance = int(row["balance"])

                    if amount > current_balance:
                        print("Insufficient balance.")
                        continue

                    row["balance"] = str(current_balance - amount)

                    print(f"New Balance: {row['balance']}")
                    break

                except ValueError:
                    print("Please enter a valid number.")

    update_file(rows)

def remove_user(username):

    rows = []

    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["username"] == username:
                continue
            rows.append(row)
    print(f'{username} is deleted')
    update_file(rows)
  


# ---------------- MENU ----------------
def menu(username):

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
                check_balance(username)

            case "2":
                deposit(username)

            case "3":
                withdraw(username)

            case "4":
                print("Logging out...")
                break

            case "5":
                print("Exiting...")
                exit()

            case _:
                print("Invalid choice.")


# ---------------- LOGIN ----------------
def login():

    while True:

        username = input("\nEnter username: ")
        
        if not user_exist(username):
            print("Username does not exist.")
            continue

        else:
            break

    tries = 3

    while tries > 0:

            password = input("Enter password: ")

            if checkpassword(username, password):

                print(f"\nWelcome {get_name(username)}!!")
                menu(username)
                return

            else:
                tries -= 1
                print(f"Incorrect password :(\n{tries} attempt(s) left")

    print("Too many failed attempts.")


# ---------------- PRINT CSV ----------------
def print_data():

    print("\nData so far:\n")

    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.DictReader(file)
        entry = 0
        for row in reader:
            print(
                f'Username = {row["username"]}, '
                f'Name = {row["name"]}, '
                f'Balance = {row["balance"]}'
            )
            entry +=1
        print(f"\nTotal entries = {entry}")

def run():

    while True:

        print("\n======= ATM =======")
        print("1. Signup")
        print("2. Login")
        print("3. Print CSV")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter choice: ")

        match choice:

            case "1":
                add_user()

            case "2":
                login()

            case "3":
                print_data()

            case "4":
                usrname = input("Enter the username u want to delete: ")
                if user_exist(usrname):
                    remove_user(usrname)
                else:
                    print("User doesn't exist ")

            case "5":
                print("Exiting...")
                break

            case _:
                print("Invalid choice.")


# ---------------- START ----------------
run()