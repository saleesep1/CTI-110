# Saleese Phillips
# 02/24/2025
# P2HW1
# Improved travel expenses program

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
print("\n-----Travel Expenses-----")
print(f"Location: {destination}")
print(f"Budget: ${budget:.2f}")
print(f"Fuel cost: ${gas:.2f}")
print(f"Hotel cost: ${hotel:.2f}")
print(f"Food cost: ${food:.2f}")
print("\n--------------------------------------------------	")
print(f"Remaining Balance: ${remaining_balance:.2f}")
