print("this is random number generator project")
import random
lower = int(input("Enter the smallest possible value: "))
upper = int(input("Enter the largest possible value: "))
random_number = random.randint(lower, upper)
print(f"Random number between {lower} and {upper} is: {random_number}")