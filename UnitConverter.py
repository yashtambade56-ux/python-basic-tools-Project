print("this is unit converter project")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Centimeters to Meters")
print("4. Kilograms to Grams")
print("5. Celsius to Fahrenheit")
print("6. Minutes to Seconds")

choice = input("Enter your choice (1/2/3/4/5/6): ")
value = float(input("Enter the value to convert: "))
if choice == '1':
    converted_value = value * 0.621371
    unit_from = "Kilometers"
    unit_to = "Miles"
elif choice == '2':
    converted_value = value / 0.621371
    unit_from = "Miles"
    unit_to = "Kilometers"
elif choice == '3':
    converted_value = value / 100
    unit_from = "Centimeters"
    unit_to = "Meters"
elif choice == '4':
    converted_value = value * 1000
    unit_from = "Kilograms"
    unit_to = "Grams"
elif choice == '5':
    converted_value = (value * 9/5) + 32
    unit_from = "Celsius"
    unit_to = "Fahrenheit"
elif choice == '6':
    converted_value = value * 60
    unit_from = "Minutes"
    unit_to = "Seconds"
else:
    converted_value = None
    unit_from = ""
    unit_to = ""

if converted_value is not None:
    print(f"{value} {unit_from} is equal to {converted_value} {unit_to}")
else:
    print("Invalid choice. Please select a valid option.")