"""

Inputs:
- name
- height
- weight
- age
- sex


Processes:
- Input validation
- Calculate BMI - (weight/height^2) * 703
- Categorize BMI
    - underwieght <18.5
    - Healthy == 18.5-24.9
    - overweight == 25.0-29.9
    - obesisty == 30.0-39.9
    - severe obesity == 40+

Outputs:
- Report for an individual

"""

# Collect Inputs
name = input("Name: ")
age = input("Age: ")
sex = input("Sex: ")
height = input("Height (inches): ")
weight = input("Weight (Pounds): ")

# Input validation
age = age.replace(".","",1)
age_is_int = age.isdigit()
if age_is_int == True:
    age = int(age)
age_is_reasonable = True
if age_is_int == True and age > 140 and age < 1:
    age_is_reasonable = False

sex = sex.lower()
sex_is_valid = False
if sex == "male" or sex == "female":
    sex_is_valid = True

height = height.replace(".","",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = False
if height_is_int == True and height > 12 and height < 140:
    height_is_reasonable = True

weight = weight.replace(".","",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = False
if weight_is_int == True and weight > 12 and weight < 1200:
    weight_is_reasonable = True


ready_to_process = True


if age_is_int == False or age_is_reasonable == False:
    print("You entered a non-expected age, please use whole numbers.")
    ready_to_process = False
    
if sex_is_valid == False:
    print("You entered a non-expected sex, please use male or female.")
    ready_to_process = False

if height_is_int == False or height_is_reasonable == False:
    print("You entered a non-expected height in inches, please use whole numbers.")
    ready_to_process = False

if weight_is_int == False or weight_is_reasonable == False:
    print("You entered a non-expected weight in pounds, please use whole numbers.")
    ready_to_process = False


if ready_to_process == True:
    bmi = (weight / height ** 2) * 703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "underweight"
    elif bmi <= 24.9:
        bmi_category = "healthy"
    elif bmi <= 29.9:
        bmi_category = "overweight"
    elif bmi <= 39.9:
        bmi_category = "obesity"
    else:
        bmi_category = "severe obesity"


    # Report
    print(f"\n"
        f"Report for {name}\n"
        f"{age} year old {sex}\n"
        f"Your BMI is {bmi:.2f}.\n"
        f"Your BMI category is: {bmi_category}"
        f"\n")