print("this is to-do list project")
list = int(input("enter number of tasks you want to add: "))
tasks = []

for i in range(list):
    tasks.append(input(f"Task {i+1}: "))

print("\nYour Tasks:")
for i, t in enumerate(tasks, 1):
    print(f"{i}. {t}")

print("All tasks added successfully!")