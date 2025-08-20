import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button]],
                   font=('Helvetica', 20))

todos = functions.get_todos()
while True:
    event, values = window.read()
    print('1: ', event)
    print('2: ', values)
    match event:
        case 'Add':
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WINDOW_CLOSED:
            break

window.close()

