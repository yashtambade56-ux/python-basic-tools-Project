print("enter the numbers for calculetion")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. square")
choice = input("enter your choice(1/2/3/4/5): ")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if choice == '1':
    result = num1 + num2
    operation = "add"
elif choice == '2':
    result = num1 - num2
    operation = "sub"
elif choice == '3':
    result = num1 * num2
    operation = "mul"
elif choice == '4':
    result = num1 / num2
    operation = "div"
elif choice == '5':
    result = num1 ** 2
    operation = "square"
else:
    result = "Invalid input"
    operation = "none"

print(f"The result of {operation}ing {num1} and {num2} is: {result}")  