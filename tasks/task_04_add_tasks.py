tasks = []
while True:
    task = input("Enter task description: ")
    if task == "":
        break
    tasks.append(task)
print('')
print('My study tasks: ')
for index, task in enumerate(tasks, start = 1):
    print(f"{index}. {task}")