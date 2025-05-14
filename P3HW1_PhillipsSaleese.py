 # Saleese Phillips

 # 03/08/2025

 #  P3LAB

 # This program takes six number grades, determines the average > displays average


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)


if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print('\nGrade Summary:')
print(f'Lowest Grade: {low:.2f}')
print(f'Highest Grade: {high:.2f}')
print(f'Total Score: {total:.2f}')
print(f'Average Score: {avg:.2f}')
print(f'Your letter grade is: {letter_grade}')
