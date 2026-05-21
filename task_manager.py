# List that stores tasks
tasks = []

# Creates a new task and adds it to the list
def add_task():

    # Gets the name of the task 
    task_name = input("What is the name of your task? ")

    # Gets the task priority level
    priority = input(f"Choose the priority level of the task '{task_name}': ")

    # Sets the value of the task to false (not completed since its a new task)
    completed = False

    # Creates a dictionary with new task data
    new_task = {"Task": task_name,
                "Priority": priority,
                "Completed": completed}
    
    # Adds task dictionary to task list
    tasks.append(new_task)

    print("Task added successfully!\n")

# Allows the user to view current task and whether the task is complete or incomplete
def view_task():

    # Checks to see if task list is empty
    if not tasks:
        print("No task availible at this time.")
        return
    
    # Loops through and displays each task
    for index, task in enumerate(tasks):
        if not task["Completed"]:
            print(f"{index + 1}.", "[ ]", task["Task"], '- ', task["Priority"])
        if task["Completed"]:
            print(f"{index + 1}.", "[X]", task["Task"], '-', task["Priority"])

def complete_task():
    # Checks to see if task list is empty
    if not tasks:
        print("No task availible at this time.")
        return
    
    view_task()

    try:
        task_number = int(input("What task did you commplete? "))
        tasks[task_number - 1]["Completed"] = True
    except ValueError:

    except IndexError:
        
    print(f"Task number {task_number} has been marked completed.")


while True:
    print()
    # Display menu options
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Exit")

    # Get user menu options
    choice = input("Choose an option: ")
    print()

    # Run selected menu features
    if choice == "1":
        add_task()
    
    elif choice == "2":
        view_task()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        break

    else:
        print("Invalid input")



