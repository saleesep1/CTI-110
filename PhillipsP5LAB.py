# Saleese Phillips
# 04/06/2025
# P5LAB

import random

def disperse_change(change_amount):
    if change_amount >= 0:

        cents = int(change_amount * 100)
        

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
        print("Cannot disperse negative change.")

def main():

    purchase_amount = round(random.uniform(0.01, 100.00), 2)
    print(f"Your total purchase amount is: ${purchase_amount:.2f}")
    

    while True:
        try:
            payment = float(input("Enter the amount of cash you will provide: $"))
            if payment < purchase_amount:
                print(f"Payment insufficient. Please provide at least ${purchase_amount:.2f}")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    

    change = payment - purchase_amount
    print(f"\nYour change is: ${change:.2f}")
    

    print("\nHere is your change breakdown:")
    disperse_change(change)


if __name__ == "__main__":
    main()