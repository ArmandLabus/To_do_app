from functions import get_todos, write_todos
import time
now = time.strftime("%d, %b, %Y  %H:%M:s")
print("It is ", now)
while True:
    #  get user input and strip space characters from it
    user_action = input("type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    # check if user action is add
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")
print("BYE")
