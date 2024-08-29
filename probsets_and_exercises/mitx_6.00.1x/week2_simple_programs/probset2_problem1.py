import math

def get_12month_balance(balance, annualInterestRate, monthlyPaymentRate):
    remainingBalance = balance
    for i in range(1,13):
        paidAmount = (monthlyPaymentRate * remainingBalance)
        interestEarned = (remainingBalance - paidAmount) * annualInterestRate/12
        remainingBalance = remainingBalance - paidAmount + interestEarned
        
        print(f"Month {i} remaining balance is {round(remainingBalance,2)}")

if __name__ == "__main__":
    balance = int(input("What is the initial balance?   "))
    annualInterestRate = float(input("What is the annual interest rate?   "))
    monthlyPaymentRate = float(input("What is the rate of amount to be paid monthly?  "))

    get_12month_balance(balance,annualInterestRate,monthlyPaymentRate)