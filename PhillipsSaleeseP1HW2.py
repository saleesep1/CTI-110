# Saleese Phillips
# 02/16/2025
# P1HW2
# This program calculates travel expenses 

# Get user input
print("This program calculates travel expenses")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate expenses
expenses = gas + hotel + food
remaining_balance = budget - expenses

# Display the results
print("\n-Travel Expenses")
print("Location:", destination)
print("Budget:", budget)
print("Fuel cost:", gas)
print("Hotel cost:", hotel)
print("Food cost:", food)
print("Remaining Balance:", remaining_balance)
