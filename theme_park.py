"""

Inputs:
- age
- day of the week
- height
- VIP
- Signed waiver
- parent present


Processes:
- Use the variables to identify which rides are available.

Outputs:
- A list of rides



"""

age = int(input("Age: "))
day_of_week = input("Day of week: ").lower()
height = int(input("Height in inches: "))
vip = input("VIP? yes/no ").lower()
signed_waiver = input("Signed waiver? yes/no ").lower()
parent_present = input("Parent present? yes/no ").lower()

# MegaDrop
"""if age >= 14  and signed_waiver == "yes" and (height >= 54 or (vip == "yes" and height >= 50)):
    print("MegaDrop")
"""


if age >=14 and signed_waiver == "yes":
    if height >= 54:
        print("MegaDrop")
    elif vip == "yes" and height >= 50:
        print("MegaDrop")

# Thunderbolt
if age >= 10 and height >= 48 and day_of_week != "monday":
    print("Thunderbolt")

# Kiddie
if age >= 8 or parent_present == "yes":
    print("Kiddie")