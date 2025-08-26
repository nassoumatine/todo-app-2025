import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

todos = functions.get_todos()

clock_label= sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="new_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todos, key="existing_todo",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, sg.Column([[edit_button], [complete_button]])],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    if event in ("Exit", sg.WINDOW_CLOSED):
        break

    window["clock"].update(value=time.strftime("%B %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            new_todo = values["new_todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window["existing_todo"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["existing_todo"][0]
                new_todo = values["new_todo"]

                index_todo_to_edit = todos.index(todo_to_edit)
                todos[index_todo_to_edit] = new_todo +"\n"
                functions.write_todos(todos)

                window["existing_todo"].update(values=todos)
            except IndexError:
                sg.popup("Please select the item to edit first.", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["existing_todo"][0]
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window["existing_todo"].update(values=todos)
            except IndexError:
                sg.popup("Please select the item to complete first.", font=("Helvetica", 20))

        case "existing_todo":
            window["new_todo"].update(value=values["existing_todo"][0])

window.close()


