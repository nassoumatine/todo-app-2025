
""""
Add actions
"""
import functions
import time

print(f"It is {time.strftime("%B %d, %Y %H:%M:%S")}.")

todos = functions.get_todos()
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos.append(todo.capitalize() + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        for index, item in enumerate(todos):
            print(f"{index+1}- {item.strip('\n')}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            if number <= len(todos):
                number -= 1
                new_todo =(input("Enter the new todo: "))
                todos[number] = new_todo.capitalize() + '\n'

                functions.write_todos(todos)
            else:
                print(f"Sorry, you only have {len(todos)} items in your to-do list.")

        except ValueError:
            print("Your command is not valid.")
            print(f"Please enter the number of the todo you want to edit. e.g. edit 2 \n")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            if number <= len(todos):
                number -= 1
                completed_todo = todos[number].strip('\n').lower()
                todos.pop(number)

                functions.write_todos(todos)

                print(f"To-do : \"{completed_todo}\" was removed from the list!")

            else:
                print(f"Sorry, you only have {len(todos)} items in your to-do list.")
        except ValueError:
            print("Your command is not valid.")
            print(f"Please enter the number of the todo you want to edit. e.g. complete 2 \n")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Oops, you entered an invalid command:(")

print("Bye!")
