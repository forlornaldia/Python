from re import I


customer_name = input("What is your name? ")
starting_balance = 5000.25
print(f"Hello {customer_name}, your balance is ${starting_balance}")
pay_check = float(input("How much of your paycheck would you like to deposit? $"))
expenditure_item = input("You were shopping recently, what did you buy? ")
expenditure = float(input(f"How much did {expenditure_item} cost? $"))

def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    customer_name = user_name
    starting_balance = balance
    paycheck = deposits
    expenditure_item = expense_item
    expenditure = expense_amount
    ending_balance = float(balance + deposits - expense_amount)
    print(f"After depositing ${deposits} and spending ${expense_amount}, you have ${ending_balance} remaining. Have a good day.")

checking_balance(customer_name, starting_balance, pay_check, expenditure_item, expenditure)