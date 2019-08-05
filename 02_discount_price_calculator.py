"""
Discount Price Calculator - www.101computing.net/discount-price-calculator/
Shopping during the sales can sometimes be very confusing. With discounted prices at 10%, 20%, 50% or even 70%!
For this challenge you are going to write a Python script that prompts the user to enter a price
(e.g. $90) and a discount rate to apply (e.g. 20%).
Your program will then calculate and display the full price, the discounted price and the savings.
"""

# Input
price = float(input('Enter the Price of item ($): '))
discount_rate = float(input('Enter the percentage discount (%): '))

# Calculations
savings = price * discount_rate/100
discounted_price = price - savings

# Program Output
print('Original Price: $', price)
print('Discounted Price: $', round(discounted_price, 2))
print('Savings: $', round(savings, 2))
