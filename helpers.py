from pathlib import Path

from options import SAVE_FILE_PATH, USAGE_MESSAGE

file_path = Path(SAVE_FILE_PATH)
empty_message = "Empty tasks list, please add some tasks and try again.\n"
category_message = """\nPlease enter a category or choose from these defaults.\n
1. Work | School\n2. Personal | Home\n3. Health & Wellness\n4. Finance\n"""


def append_helper(task, cat):
    with open(file_path, "a") as f:
        f.write(f"[][{cat}]: {task}\n")


def category_helper(task):
    print(category_message)

    input_a = input("Enter your choice: ")

    match input_a:
        case "1":
            print("\nWork | School category assigned.")
            append_helper(task, "Work | School")
        case "2":
            print("\nPersonal | Home category assigned.")
            append_helper(task, "Personal | Home")
        case "3":
            print("\nHealth & Wellness category assigned.")
            append_helper(task, "Health & Wellness")
        case "4":
            print("\nFinance category assigned.")
            append_helper(task, "Finance")
        case _:
            if not input_a:
                print("\nNo category assigned.")
                append_helper(task, "None")
            else:
                print(f"\n{input_a.strip()} category assigned.")
                append_helper(task, (input_a.strip()))

    print(f""""{task}" added successfully.""")


def editing_helper():
    pass


def text_list_builder():
    with open(file_path, "r") as f:
        read = f.read()

    texts = read.split("\n")
    new_texts = []

    for text in texts:
        if text:
            if text.startswith("[]"):
                new_texts.append("(Incomplete)" + text[2:])
            if text.startswith("[x]"):
                new_texts.append("(Complete)" + text[3:])

    if not new_texts:
        print(empty_message)
        return
    return new_texts


def message_helper():
    if USAGE_MESSAGE == 1:
        print(
            '\nUsage: "add" or "a" to add tasks, "delete" or "d" to delete tasks, "view" or "v" for viewing tasks, "edit" or "e" for editing tasks.\nTasks are saved in a ".txt" file in the program directory by default.\n'
        )
    elif USAGE_MESSAGE == 0:
        return
