"""
Jonathan Thompson
IS 303

Inputs:

- Student name
- Grade for three classes
- Credits for three classes

Processes:

- Calculate the GPA using the grades and the credits total

Outputs:

- GPA
- Report card for student

"""


# Inputs
name = input("Student name: ")
grade1 = int(input("Course 1 grade point: "))
grade2 = int(input("Course 2 grade point: "))
grade3 = int(input("Course 3 grade point: "))
credit1 = int(input("Course 1 credits: "))
credit2 = int(input("Course 2 credits: "))
credit3 = int(input("Course 3 credits: "))


# Processes

total_credits = credit1 + credit2 + credit3
gpa = (grade1*credit1 + grade2*credit2 + grade3*credit3)/total_credits

# Outputs

print(f"{name}'s Report Card")
print(f"Credit  taken: {total_credits}")
print(f"Course 1: {grade1} credits: {credit1}\n"
      f"Course 2: {grade2} credits: {credit2}\n"
      f"Course 3: {grade3} credits: {credit3}")
print(f"GPA: {gpa:.2f}")

