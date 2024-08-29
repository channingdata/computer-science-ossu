import math

def get_min_payment_to_clear_12months(balance, annualInterestRate):

    for min_payment in range(10,balance, 10):
        remainingBalance = balance
        
        for month in range(1,13):
            interestEarned = (remainingBalance - min_payment) * annualInterestRate/12
            remainingBalance = remainingBalance - min_payment + interestEarned
        
        if remainingBalance <= 0:
            print(f"---The minimum monthly payment should be {min_payment} to clear the debt in 12 months--")
            break
        else:
            print(f"Monthly amount of {min_payment} is not enoug. Remaining Balance is {remainingBalance}")

if __name__ == "__main__":
    balance = int(input("What is the initial balance?   "))
    annualInterestRate = float(input("What is the annual interest rate?   "))

    get_min_payment_to_clear_12months(balance,annualInterestRate)