import math

def get_min_payment_to_clear_12months_bisection(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12
    monthlyPaymentLB = round(balance/12, 2)
    monthlyPaymentUB = round((balance * (1 + monthlyInterestRate)**12)/12,2)

    while True:
        bound_range = (monthlyPaymentUB - monthlyPaymentLB)
        min_payment = round(monthlyPaymentLB + bound_range/2, 2)
        remainingBalance = balance
        for month in range(1,13):
            interestEarned = (remainingBalance - min_payment) * monthlyInterestRate
            remainingBalance = remainingBalance - min_payment + interestEarned
        
        if remainingBalance == 0 or (bound_range <= 0.01 and remainingBalance < 0):
            print(f"---The minimum monthly payment should be {min_payment} to clear the debt in 12 months--")
            break
        elif remainingBalance > 0:
            print(f"Monthly amount of {min_payment} is not enough (Range: {monthlyPaymentLB}-{monthlyPaymentUB}. {bound_range}). Remaining Balance is {remainingBalance}")
            
            if bound_range <= 0.01:
                monthlyPaymentLB = monthlyPaymentUB
            else:
                monthlyPaymentLB = min_payment
        else:
            print(f"Monthly amount of {min_payment} is not enough (Range: {monthlyPaymentLB}-{monthlyPaymentUB}. {bound_range}). Remaining Balance is {remainingBalance}")
            monthlyPaymentUB = min_payment

if __name__ == "__main__":
    balance = int(input("What is the initial balance?   "))
    annualInterestRate = float(input("What is the annual interest rate?   "))

    get_min_payment_to_clear_12months_bisection(balance,annualInterestRate)
