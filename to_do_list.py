tasks = []

while True:
    task = input("Enter task (or 'quit'): ")
    if task.lower() == "quit":
        break
    tasks.append(task)

print("Tasks:")
for t in tasks:
    print("-", t)