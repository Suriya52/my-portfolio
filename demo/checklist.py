checklist = {
    "Task 1": True,  
    "Task 2": False, 
    "Task 3": True,  
    "Task 4": False, 
}


completed_tasks = []
incomplete_tasks = []


for task, is_completed in checklist.items():
    if is_completed:
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)


print("Completed tasks:", completed_tasks)
print("Incomplete tasks:", incomplete_tasks)
