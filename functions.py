import os

from helpers import (
    category_helper,
    category_message,
    file_path,
    message_helper,
    text_list_builder,
)
from options import SAVE_FILE_PATH

file_path.touch(exist_ok=True)


def menu():
    inp = input("Enter 1 to enter the program or 2 to exit it.\n")
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


def add():
    input_a = input("Please enter the task: ")
    task = None
    if input_a:
        task = input_a
        category_helper(task)
    if not input_a:
        print("Empty input recieved, please try again.")
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
    invalid_message = "Invalid index, please try again."

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
            input_e = input("\nEnter 1 to edit the task or 2 to edit the category: ")

            if input_e != "1" or input_e != "2":
                print("\nInvalid choice recieved, please try again.\n")

            if input_e == "1":
                input_e = input("\nPlease enter the task: ")

                if input_e == 0 or not input_e:
                    print("Empty task recieved, please try again.")
                    return

                new_task = old_task.copy()
                new_task[1] = input_e
                new_task = ": ".join(new_task)

                viewed[index] = new_task

                open(file_path, "w").close()

                for text in viewed:
                    if text.startswith("(Incomplete)"):
                        with open(file_path, "a") as f:
                            f.write("[]" + text[12:] + "\n")

                    if text.startswith("(Complete)"):
                        with open(file_path, "a") as f:
                            f.write("[x]" + text[10:] + "\n")

                print(f'\nChanged "{": ".join(old_task)}" to "{viewed[index]}"\n')

            if input_e == "2":
                print(category_message)

                input_e = input("Enter your choice: ")
                old_task = viewed[index].split(": ")
                old_task[0] = old_task[0].split(")")

                print(old_task)

                if not input_e:
                    print("\nEmpty category recieved, please try again.\n")

    except ValueError:
        print(invalid_message)
