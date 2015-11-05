totalPayment = 0.00
monthlyInterestRate = annualInterestRate / 12.0
for month in range(1, 13):
    monthlyPayment = monthlyPaymentRate * balance
    totalPayment += monthlyPayment
    monthlyUnpaidBalance = balance - monthlyPayment
    balance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
    print 'Month: ', month
    print 'Minimum monthly payment: ', round(monthlyPayment, 2)
    print 'Remaining balance: ', round(balance, 2)
print 'Total Paid: ', round(totalPayment, 2)
print 'Remaining balance: ', round(balance, 2)