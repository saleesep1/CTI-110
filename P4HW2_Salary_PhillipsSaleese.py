
# Saleese Phillips
# 03/21/2025
# P4HW2
# This program outputs employee salary. including the pay raise for overtime
# The user inputs employee name, hours worked, and pay.
# The program  will calculates regular pay, overtime pay, and gross pay. 
# Improved program , determines pay of regular and overtime for multiple employees and closes when you write Done


total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter employee's name (or 'Done' to exit): ")
    if employee_name.lower() == "done":
        break

    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    REGULAR_HOURS = 40
    OVERTIME_RATE = 1.5

    overtime_hours = max(0, hours_worked - REGULAR_HOURS)
    regular_hours = min(hours_worked, REGULAR_HOURS)
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * OVERTIME_RATE)
    gross_pay = regular_pay + overtime_pay

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    print("\n--------------------------------------------------")
    print(f"Employee name: \t {employee_name}")
    print("--------------------------------------------------")
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<13.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f} ${overtime_pay:<12.2f} ${regular_pay:<12.2f} ${gross_pay:<12.2f}")

if employee_count > 0:
    print("\n========================================================")
    print(f"Total number of employees entered: {employee_count}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross pay: ${total_gross_pay:.2f}")
    print("========================================================")
