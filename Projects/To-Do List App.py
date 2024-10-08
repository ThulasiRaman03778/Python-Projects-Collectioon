# Simple To-Do List
def display_tasks(tasks):
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def main():
    tasks = []
    while True:
        display_tasks(tasks)
        action = input("Type 'add' to add a task, 'remove' to remove a task, or 'quit' to exit: ")

        if action == "add":
            task = input("Enter the task: ")
            tasks.append(task)
        elif action == "remove":
            task_num = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks.pop(task_num)
            else:
                print("Invalid task number.")
        elif action == "quit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

