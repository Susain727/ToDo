class ToDo_list:
    def __init__(self):
        self.tasks = []
    
    def display_menu(self):
        print("\n____Display Menu____")
        print("1. Add task")
        print("2. Edit task")
        print("3. Delete task")
        print("4. Display task")
        print("5. Exit")

    def add_task(self):
        print("\n___Add Task___")
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added succesfully")
    
    def edit_task(self):
        if self.tasks:
            self.display_task()
            index = int(input("Enter the task index to edit: ")) -1
            if 0<= index < len(self.tasks):
                new_task = input("enter your new task: ")
                self.tasks[index] = new_task
                print("Task edited succesfully")
            else:
                print("Invalid index")
        else:
            print("No task to edit.")
    def delete_task(self):
        if self.task:
            self.display_task()
            index = int(input("Enter the task index to delete: ")) -1
            if 0<= index < len(self.tasks):
                self.tasks.pop(index)
                print("Task deleted succesfully")
            else:
                print("Invalid syntax")
        else:
            print("No task to delete.")
        
    def display_task(self):
        print("____Displaying tasks_____")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("select an option: ")
            if choice == '1':
                self.add_task()
            
            elif choice == '2':
                self.edit_task()
            
            elif choice == '3':
                self.delete_task()
            
            elif choice == '4':
                self.display_task()
            
            elif choice == '5':
                print("Exiting, Goodbye")
                break

            else:
                print("Invalid Syntax")


todo = ToDo_list()
todo.run()