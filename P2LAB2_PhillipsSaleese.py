# 02-20-2025
# P2LAB2
# This program lets the user choose a vehicle and calculates the fuel needed for a trip.


vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}


print("Available vehicles:", vehicles.keys())


vehicle = input("\nEnter a vehicle to see its mpg: ")


if vehicle in vehicles:
    mpg = vehicles[vehicle]
    print(f"\nThe {vehicle} gets {mpg} mpg.")

    miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))


    gallons = miles / mpg


    print(f"\nYou will need {round(gallons, 2)} gallon(s) of gas.")
else:
    print("\nThat vehicle is not in the list. Try again.")