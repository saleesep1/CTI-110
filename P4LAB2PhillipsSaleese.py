
# Saleese Phillips
# 03/19/2025
# P4Lab1
# Multiplcation table program

while True:
    num = int(input("Enter an integer: "))
    if num >= 0:
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
    else:
        print("Cannot accept negative values.")
    again = input("Do you wish to run it again? (yes/no): ").lower()
    if again != "yes":
        break