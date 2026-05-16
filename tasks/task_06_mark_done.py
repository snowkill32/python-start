tasks = [
    {"title": "Learn dict", "status": "active"},
    {"title": "Learn lists", "status": "active"},
    {"title": "Learn loops", "status": "active"}
]
print("My tasks: ")
for index, task in enumerate(tasks, start = 1):
    print(f'{index}. {task["title"]} | status: {task["status"]}')
choice = int(input("Enter task number to mark done: ")) - 1
if len(tasks) >= choice:
    tasks[choice]["status"] = 'done'
    print("Updated tasks: ")
    for index, task in enumerate(tasks, start = 1):
        print(f'{index}. {task["title"]} | status: {task["status"]}')
else:
    print('incorrect number, more then amount of tasks')
    