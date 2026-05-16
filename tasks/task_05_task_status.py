tasks = [
    {"title": "Learn dict", "status": "active"},
    {"title": "Learn lists", "status": "active"},
    {"title": "Learn loops", "status": "active"}
]
print("My tasks: ")
for index, task in enumerate(tasks, start = 1):
    print(f'{index}. {task["title"]} | status: {task["status"]}')