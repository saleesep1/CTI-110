
Pseudocode:
# 1. empty list named `grades`.
# 2 ask for input for each module -> store in grades variable
# 3.show lowest grade using the min function 
# 4.show lowest grade using the max function 
# 5.show sum using sum function
# 6.show the average by dividing the sum by the number of grades, formatting it to two decimal places.
# 7.Print the results


grades = []


grades.append(int(input("Enter grade for Module 1: ")))
grades.append(int(input("Enter grade for Module 2: ")))
grades.append(int(input("Enter grade for Module 3: ")))
grades.append(int(input("Enter grade for Module 4: ")))
grades.append(int(input("Enter grade for Module 5: ")))
grades.append(int(input("Enter grade for Module 6: ")))


print("Lowest grade:  ", min(grades))
print("Highest grade: ", max(grades))
print("Sum of grades: ", sum(grades))
print("Average grade: {:.2f}".format(sum(grades) / len(grades)))
