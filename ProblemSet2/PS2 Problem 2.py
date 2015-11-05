def balance_left(balance, monthlyPayment):
    remainingBalance = balance
    for month in range(1, 13):
        monthlyUnpaidBalance = remainingBalance - monthlyPayment
        remainingBalance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
    return round(remainingBalance, 2)

monthlyInterestRate = annualInterestRate / 12.0
for payment in range(0, balance, 10):
    unpaid_balance = balance_left(balance, payment)
    if unpaid_balance <= 0:
        print 'Lowest payment: ', payment
        break