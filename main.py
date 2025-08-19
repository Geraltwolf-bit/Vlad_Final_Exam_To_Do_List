#initialize the to_do_list outside of all functions as a global variable:
to_do_list = []

#create a function that adds tasks to the system
def add_task():
  while True:
    task = input("Enter task or 'done' to finish: ")
    if task.lower() == 'done':
      print("\n")
      print("Your list is formed.")
      print("\n")
      break
    else:
      to_do_list.append(task)
      print("\n")
      print("Task added.")
      print("\n")

#create a function that shows the list
def see_list():
  if not to_do_list:
    print("\n")
    print("Your list is empty.")
    print("\n")
  else:
    print("\nYour list:")
    for i, task in enumerate(to_do_list, 1):
      print(f"{i}. {task} ")
    print()

#create a function that deletes tasks from the system
def delete_task():
  see_list()
  while True:
    task_num = int(input("Enter the the task number to delete or '0' to return: "))
    if 1 <= task_num <= len(to_do_list):
      deleted_task = to_do_list.pop(task_num - 1)
      print("\n")
      print("Deleted task:", deleted_task)
      print("\n")
      see_list()
    elif task_num == 0:
      print("\n")
      print("Exciting delete menu.")
      print("\n")
      break  

#create the main function that unifies all function in one program
def main_menu():
  while True:
    print("To see your list, enter: 1")
    print("To add a task, enter: 2")
    print("To delete a task, enter: 3")
    print("To exit, enter: 4")

    command = input("Enter your command as a digit: ")
    if command == '1':
      see_list()
    elif command == '2':
      add_task()
    elif command == '3':
      delete_task()
    elif command == '4':
      print("\n")
      print("Have a nice day!")
      print("\n")
      break
    else:
      print("\n")
      print("Wrong input. Try again: '1', '2', '3', or '4'")
      print("\n")

#create a function that starts the program and greets the user
if __name__ == "__main__":
  print("\n")
  print("Welcome to To_Do_List!")
  print("\n")
  main_menu()