account_balance = int(input("Enter your Account Balance : "))
withdrawal_amount = int(input("Enter your Withdrawal Amount : "))

new_balance = account_balance - withdrawal_amount

if withdrawal_amount > account_balance:
    print("Insufficient Funds.")
elif withdrawal_amount % 100 != 0:
    print("Invalid Amount.")
elif  withdrawal_amount % 100 == 0:
    print ("Withdrawal successful!")
    print (f"your account balance is {new_balance}.")
    if new_balance < 1000:
        print("Low Balance.")


