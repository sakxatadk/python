balance = 100000

print("\n Welcome to the ATM Machine \n")
print("1. Check Balance")
print("2. Deposit ")
print("3. Withdraw ")
print("4. Exit ")

choice = int(input("Enter your choice:"))
match (choice):
    case 1:
        print(f"Your total balance is {balance}")
    case 2:
        amount = int(input("Enter the amount to deposit:"))
        balance = balance + amount
        print(f"Your total balance is {balance}")
    case 3:
        withdraw = int(input("Enter the amount you want to withdraw:"))
        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance = balance - withdraw
            print(f"Please collect your cash\nYour total balance is {balance}")
    case 4:
        print("Thank you for using the ATM Machine")
    case _:
        print("Invalid choice") 
    
