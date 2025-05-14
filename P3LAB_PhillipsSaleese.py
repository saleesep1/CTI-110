
amount = input("Enter a monetary amount (e.g., 4.37): ")

if "." in amount:
    amount = float(amount)
    if amount >= 0:
        cents = int(amount * 100)
        
        dollars = cents // 100
        cents %= 100
        quarters = cents // 25
        cents %= 25
        dimes = cents // 10
        cents %= 10
        nickels = cents // 5
        cents %= 5
        pennies = cents
        
        if dollars > 0:
            print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
        if quarters > 0:
            print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
        if dimes > 0:
            print(f"{dimes} dime{'s' if dimes > 1 else ''}")
        if nickels > 0:
            print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
        if pennies > 0:
            print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
    else:
        print("Please enter a positive amount.")
else:
    print("Invalid input. Please enter a valid number.")