
# Saleese Phillips
# 03/16/2025
# P3HW2
# This program outputs employee salary. including the pay raise for overtime
# The user inputs employee name, hours worked, and pay.
# The program  will calculates regular pay, overtime pay, and gross pay. 



employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


REGULAR_HOURS = 40
OVERTIME_RATE = 1.5


overtime_hours = max(0, hours_worked - REGULAR_HOURS)
regular_hours = min(hours_worked, REGULAR_HOURS)
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * OVERTIME_RATE)
gross_pay = regular_pay + overtime_pay


print("\n--------------------------------------------------")
print(f"Employee name: \t {employee_name}")
print("--------------------------------------------------")
print("Hours Worked   Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<13.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f} ${overtime_pay:<12.2f} ${regular_pay:<12.2f} ${gross_pay:<12.2f}")
