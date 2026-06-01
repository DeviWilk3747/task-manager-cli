class TaskManager:

    def __init__(self):
        self.tasks = []
    
    def add_task(self):

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
        self.tasks.append(new_task)

        self.save_tasks()

        print("Task added successfully!\n")

    def view_task(self):

     # Checks to see if task list is empty
        if not self.tasks:
           print("No task availible at this time.")
           return
    
        # Loops through and displays each task
        for index, task in enumerate(self.tasks):
            if not task["Completed"]:
                print(f"{index + 1}.", "[ ]", task["Task"], '- ', task["Priority"])
            else:
                print(f"{index + 1}.", "[X]", task["Task"], '-', task["Priority"])
    
    # Allows user to edit existing tasks 
    def edit_task(self):

    # Checks to see if task list is empty
        if not self.tasks:
            print("No task availible at this time.")
            return
    
        # Displays current tasks to the user
        self.view_task()

        try:
            # Gets the task number the user wants to edit
            choose_task = int(input("Choose a task you would like to edit. "))

            # Stores the selected task dictionary
            selected_task = self.tasks[choose_task - 1]

            # Updates the task name
            selected_task["Task"] = input("What is the new name of your task? ")

            # Updates the task priority
            selected_task["Priority"] = input("What is the new priority level of your task? ")

            # Saves updated task data to file
            self.save_tasks()

            # Confirms successful update
            print("Task updated successfully")
    
        # Handles invalid number input
        except ValueError:
            print("Please enter a valid task number.")

        # Handles task number that do not exist
        except IndexError:
            print("Task number does not exist")


    def complete_task(self):

        # Checks to see if task list is empty
        if not self.tasks:
            print("No task availible at this time.")
            return
    
        self.view_task()

        try:
            task_number = int(input("What task did you commplete? "))
            self.tasks[task_number - 1]["Completed"] = True
            self.save_tasks()
            print(f"Task number {task_number} has been marked completed.")

        except ValueError:
            print("Please enter a valid task number.")
        
        except IndexError:
            print("Task number doesn't exist.")

    # Allows user to view and select a task to delete
    def delete_task(self):

        # Checks to see if task list is empty
        if not self.tasks:
            print("No task availible at this time.")
            return
    
        self.view_task()

        try:
            task_delete = int(input("What task number would you like to delete? \n"))

            removed_task = self.tasks.pop(task_delete - 1)
            self.save_tasks()
            print(f"'{removed_task['Task']}' removed successfully.\n")

        except ValueError:
            print("Please enter a valid task number.")

        except IndexError:
            print(f"Task number {task_delete} could not be found.\n")

    def save_tasks(self):
        file = open("Task_Manager.txt", "w")

        for task in self.tasks:
            file.write(f"{task['Task']}, {task['Priority']}, {task['Completed']}\n")

        file.close()

    def load_tasks(self):

        try:
            file = open("Task_Manager.txt", "r")
        except FileNotFoundError:
            return
    
        for line in file:
            parts = line.split(",")

            task_name = parts[0].strip()
            priority = parts[1].strip()
            completed_status = parts[2].strip()

            if completed_status == "True":
                completed_status = True
            else:
                completed_status = False
        
            task = {
                "Task": task_name,
                "Priority": priority,
                "Completed":completed_status}
        
            self.tasks.append(task)
        file.close()

    def run(self):
        while True:
            print()
            # Display menu options
            print("1. Add Task")
            print("2. View Task")
            print("3. Complete Task")
            print("4. Delete Task")
            print("5. Edit Task")
            print("6. Exit")

            # Get user menu options
            choice = input("Choose an option: ")
            print()

            # Run selected menu features
            if choice == "1":
                manager.add_task()
    
            elif choice == "2":
                manager.view_task()

            elif choice == "3":
                manager.complete_task()

            elif choice == "4":
                manager.delete_task()

            elif choice == "5":
                manager.edit_task()

            elif choice == "6":
                break

            else:
                print("Invalid input")


manager = TaskManager()
manager.load_tasks() 
manager.run()

