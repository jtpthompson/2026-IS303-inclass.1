"""
Code written with a bug hidden for a competiton where you have to hunt for a bug.

The code itself is a simple age validation program that checks if the inputted age is a number and within a reasonable range.

"""

age = input("Age: ")
age_validation = age.replace(".","",1)
age_is_int = age_validation.isdigit()
if age_is_int == True:
    #The bug is here. Should be age = float(age) because we want to allow for decimal ages, but the code is trying to convert it to an int which will cause an error if the user enters a decimal age.
    age = int(age)
elif age_is_int == False:
    print("Invalid age. Please enter a number.")
age_is_reasonable = False
if age_is_int == True and age < 140 and age > 1:
    age_is_reasonable = True
    print(f"Your age is {round(age,1)}")
else:
    print("Caution: Age entered is unreasonable.")
