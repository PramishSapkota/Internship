users = {
    "alice": {"passcode": "1234", "balance": 1000},
    "bob": {"passcode": "5678", "balance": 500},
    "charlie": {"passcode": "9101", "balance": 2000}
}

while True:

    username = input("\nEnter username: ")

    if username not in users:
        print("Username does not exist.")
        continue

    tries = 3

    while tries > 0:

        password = input("Enter password: ")

        if password == users[username]["passcode"]:

            print(f"\nWelcome {username}!")

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
                        print(f"Balance: {users[username]['balance']}")

                    case "2":
                        deposit_amount = int(input("Enter deposit amount: "))

                        if deposit_amount > 0:
                            users[username]["balance"] += deposit_amount
                            print(f"New Balance: {users[username]['balance']}")
                        else:
                            print("Invalid amount.")

                    case "3":
                        withdraw_amount = int(input("Enter withdraw amount: "))

                        if withdraw_amount <= 0:
                            print("Invalid amount.")

                        elif withdraw_amount <= users[username]["balance"]:
                            users[username]["balance"] -= withdraw_amount
                            print(f"New Balance: {users[username]['balance']}")

                        else:
                            print("Insufficient balance.")

                    case "4":
                        print("Logging out...")
                        break

                    case "5":
                        print("Exiting program...")
                        exit()

                    case _:
                        print("Invalid choice.")

            break

        else:
            tries -= 1
            print(f"Wrong password :( \n---{tries}attempt(s) left--- ")

    else:
        print("All attempts exhausted.")
        print("Exiting..")
        break
    # break

'''
Enter username: bob
Enter password: 5678

Welcome bob!

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 1
Balance: 500

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 2
Enter deposit amount: -0
Invalid amount.

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 2
Enter deposit amount: 0
Invalid amount.

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 2
Enter deposit amount: 100
New Balance: 600

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 1
Balance: 600

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 3
Enter withdraw amount: 1000
Insufficient balance.

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 200
Invalid choice.

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 3
Enter withdraw amount: 200
New Balance: 400

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 4
Logging out...

Enter username: bob
Enter password: 5678

Welcome bob!

====== MENU ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout
5. Exit
Enter choice: 5
Exiting program...
'''