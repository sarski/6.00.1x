def balance_left(balance, monthlyPayment):
    remainingBalance = balance
    for month in range(1, 13):
        monthlyUnpaidBalance = remainingBalance - monthlyPayment
        remainingBalance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
    return round(remainingBalance, 2)

monthlyInterestRate = annualInterestRate / 12.0
lowMonthlyPayment = balance / 12
highMonthlyPayment = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
avgMonthlyPayment = (lowMonthlyPayment + highMonthlyPayment) / 2
avg_balance = balance_left(balance, avgMonthlyPayment)
while avg_balance < -0.01 or avg_balance > 0.01:
    if avg_balance > 0.01:
        lowMonthlyPayment = avgMonthlyPayment
    elif avg_balance < 0.01:
        highMonthlyPayment = avgMonthlyPayment
    avgMonthlyPayment = (lowMonthlyPayment + highMonthlyPayment) / 2
    avg_balance = balance_left(balance, avgMonthlyPayment)
print 'Lowest payment: ', round(avgMonthlyPayment, 2)