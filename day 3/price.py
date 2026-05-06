"""
A Price validation program that checks if the price entered is a number and within a reasonable range.



"""


price = input("Price: ")
price_validation = price.replace(".","",1)
price_is_int = price_validation.isdigit()
if price_is_int == True:
    price = float(price)
elif price_is_int == False:
    print("Invalid price. Please enter a number.")
price_is_reasonable = False
if price_is_int == True and price <= 10000 and price >= 100:
    price_is_reasonable = True
elif price_is_int == True and price <= 20000 and price >= 10:
    price_is_reasonable = True
    print("Caution: Price entered is outside of the average price range of $100-$1000.")
else:
    print("Please enter a valid price within the range of $10-$2000")

if price_is_reasonable:
    print(f"The price is ${round(price,2):.2f}")