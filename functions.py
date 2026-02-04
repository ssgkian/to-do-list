import os

from helpers import (
    category_helper,
    category_message,
    file_path,
    message_helper,
    text_list_builder,
    writing_helper,
)
from options import SAVE_FILE_PATH

file_path.touch(exist_ok=True)


def menu():
    inp = input("Enter 1 to enter the program, or 2 to exit it.\n")
    if inp == "1":
        input_handler()
    if inp == "2":
        print("Exiting program...")
        exit()
    if not inp:
        print("Exiting program...")
        exit()


def input_handler():
    message_helper()
    while True:
        inp = input("Enter your choice: ")
        if inp == "add" or inp == "a":
            add()
        if inp == "view" or inp == "v":
            _ = view()
        if inp == "edit" or inp == "e":
            edit()
        if inp == "mark" or inp == "m":
            mark()


def add():
    input_a = input("Please enter the task: ")
    task = None
    if input_a:
        task = input_a
        category_helper(task)
    if not input_a:
        print("Empty input recieved, please try again.\n")
        return


def view():
    print("")
    new_texts = text_list_builder()
    if not new_texts:
        return
    for i, text in enumerate(new_texts, start=1):
        print(f"{i}. {text}")
    print("")
    return new_texts


invalid_message = "\nInvalid index, please try again.\n"


def edit():
    viewed = view()
    if not viewed:
        return
    elif len(viewed) == 0:
        return

    length = len(viewed)
    index = None
    old_task = None
    new_task = None
    new_text = None
    status = None
    category = None

    try:
        input_e = int(input("Please enter the index of the task you want to edit: "))
        if input_e == 0:
            print(invalid_message)
            return

        if input_e:
            if input_e > length:
                print(invalid_message)
                return

            index = input_e - 1
            print(f'\nEditing "{viewed[index]}"')
            old_task = viewed[index].split(": ")
            input_e = input("\nEnter 1 to edit the task, or 2 to edit the category: ")

            if input_e == "1":
                input_e = input("\nPlease enter the task: ")

                if input_e == 0 or not input_e:
                    print("Empty task recieved, please try again.\n")
                    return

                new_task = old_task.copy()
                new_task[1] = input_e
                new_task = ": ".join(new_task)

                viewed[index] = new_task

                writing_helper(viewed)

                print(f'\nChanged "{": ".join(old_task)}" to "{viewed[index]}"\n')

            if input_e == "2":
                print(category_message)
                input_e = input("\nEnter your choice: ")

                if not input_e:
                    print("\nEmpty category recieved, please try again.\n")
                    return

                old_task = viewed[index].split(": ")
                status, category = old_task[0].split("[")
                status, category = status.strip("()"), category.strip("[]")

                match input_e:
                    case "1":
                        category = "[Work | School]"
                        print("\nWork | School category assigned.\n")
                    case "2":
                        category = "[Personal | Home]"
                        print("\nPersonal | Home category assigned.\n")
                    case "3":
                        category = "[Health & Welness]"
                        print("\nHealth & Wellness category assigned.\n")
                    case "4":
                        category = "[Finance]"
                        print("\nFinance category assigned.\n")
                    case _:
                        category = f"[{input_e.strip()}]"
                        print(f'\n"{input_e.strip()}" category assigned.\n')

                status = "(" + status + ")"

                new_text = status + category + ": " + old_task[1].strip()
                viewed[index] = new_text

                writing_helper(viewed)

    except ValueError:
        print(invalid_message)


def mark():
    viewed = view()
    if not viewed:
        return
    elif len(viewed) == 0:
        return

    length = len(viewed)
    text = None
    try:
        input_e = int(input("Please enter the index of the task you want to mark: "))
        if input_e == 0:
            print(invalid_message)
            return
        if input_e:
            if input_e > length:
                print(invalid_message)
                return
            index = input_e - 1
            print(f'\nMarking "{viewed[index]}"\n')

            input_e = int(
                input("Enter 1 to mark the task as Complete, or 2 for Incomplete: ")
            )

            if input_e != 1 and input_e != 2:
                print("\nInvalid choice, please try again.\n")
                return

            task_to_mark = viewed[index].split(": ")
            status, category = task_to_mark[0].split("[")
            status, category = status.strip("()"), category.strip("[]")
            category = "[" + category + "]"

            if input_e == 1:
                if status == "Incomplete":
                    status = "(" + "Complete" + ")"
                    print("\nSuccesfully marked task as complete.\n")
                else:
                    print(
                        "\nThe task is already marked as Complete, please try again.\n"
                    )
                    return

            elif input_e == 2:
                if status == "Complete":
                    status = "(" + "Incomplete" + ")"
                    print("\nSuccessfully marked task as incomplete.\n")
                else:
                    print(
                        "\nThe task is already marked as Incomplete, please try again.\n"
                    )
                    return

            text = status + category + ": " + task_to_mark[1].strip()
            viewed[index] = text
            print(f"{viewed[index]}\n")
            writing_helper(viewed)

    except ValueError:
        print("\nInvalid choice, please try again.\n")


def delete():
    pass
