# Here you will implememnt your fist todo list in python.

list_Todo = []

def add_todo() -> dict:
    """
    Add a new todo task to the list_Todo.
    """
    # The task should contains at least three keys
    # task: str, description: str, completed: bool

    # It should look something like this 
    # {
    #     "task": "Task 1",
    #     "description": "This is a description",
    #     "completed": False
    # }
    
    # Add your implementation here
    pass

def remove_todo() -> dict:
    """
    Remove a todo task from the list_Todo.
    """
    # The task should be removed by its index in the list_Todo
    # Add your implementation here
    pass

def update_todo(index: int) -> dict:
    """
    Update a todo task in the list_Todo.
    """
    # The task should be updated by its index in the list_Todo
    # Add your implementation here
    pass

def list_todo(todo_list: list) -> None:
    """
    List all todo task in the list_Todo.
    """
    # Add your implementation here
    for task in todo_list:
        print(f"Task: {task['task']}")
        print(f"Description: {task['description']}")
        print(f"Completed: {task['completed']}")


def main():
    number_task = int(input("Enter the number of task you want to add: "))
    for _ in range(number_task):
        add_todo()
    modify = input("Do you want to modify any task? (yes/no): ")
    if modify == "yes":
        index = int(input("Enter the index of the task you want to modify: "))
        update_todo(index)
    else :
        pass
    remove = input("Do you want to remove any task? (yes/no): ")
    if remove == "yes":
        index = int(input("Enter the index of the task you want to remove: "))
        remove_todo()
    else:
        pass
    list_todo(list_Todo)