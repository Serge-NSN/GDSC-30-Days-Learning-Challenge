# Program that converts weight of user from pounds to kilogram and vice versa
print("Hi! Please input 1 or 2 depending on what you want to convert")
user_input = input("1. Pounds to Kilograms conversion\n2. Kilograms to Pounds conversion\n")
if user_input == '1':
    user_weight = float(input("Please enter your weight in Pounds\n"))
    print(f"Your {user_weight} pounds weight in kilograms is {user_weight*0.454}kg\n")
elif user_input == '2':
    user_weight = float(input("Please enter your weight in kilograms\n"))
    print(f"Your {user_weight} kilograms weight in pounds is {user_weight/0.454}pounds\n")
else:
    print("Please input the right option. Either '1' or '2'")
