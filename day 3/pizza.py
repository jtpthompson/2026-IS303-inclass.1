food = "pizza"

if food == "burger" or "pizza":
    print("Fast food!")

age = input("Age: ")
if int(age) < 0:
    print("Invalid age")
elif int(age) < 18:
    print("Minor")
else:
    print("Adult")

name = "Alice"
result = name.lower()

print(name)
print(result)