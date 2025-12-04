print("this is project file with 5 basic projects")
print("1. calculater")
print("2. Password Generator")
print("3. Unit Converter")
print("4. To-Do List")
print("5. Random Number Generator")
print("6. Exit")

choice = input("enter your choice(1/2/3/4/5/6): ")

if choice == '1':
    import Calculator
elif choice == '2':
    import PasswordGenerator
elif choice == '3':
    import UnitConverter
elif choice == '4':
    import ToDoList
elif choice == '5':
    import RandomNumberGenerator
elif choice == '6':
    print("Exiting the program.")
else:
    print("Invalid input")