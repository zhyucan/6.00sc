# !/usr/bin/env python
# -*- coding:utf-8 -*-

# Paying Off Credit Card Debt

# Paying the Minimum

# Problem 1

# balance = float(raw_input('balance: '))
# annual_rate = float(raw_input('annual interest rate: '))
# min_mon_rate = float(raw_input('minimum monthly payment rate: '))
#
# total = 0
# remain = 0
#
# for i in range(1, 13):
#     min_mon_pay = round(min_mon_rate * balance, 2)
#     interest = annual_rate / 12 * balance
#     principle = round(min_mon_pay - interest, 2)
#     remain = round(balance - principle, 2)
#     print 'Month: {}'.format(i)
#     print 'Minimum monthly payment: ${}'.format(min_mon_pay)
#     print 'Principle paid: ${}'.format(principle)
#     print 'Remaining balance: ${}'.format(remain)
#
#     total += min_mon_pay
#     balance -= round(principle, 2)
#
# print('RESULT')
# print('Total amount paid: ${}'.format(total))
# print('Remaining balance: ${}'.format(remain))


# Paying Debt Off In a Year

# Problem 2

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))


