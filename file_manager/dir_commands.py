import os

full_path = ""


def create_directory(string):
    try:
        os.mkdir(full_path + string, mode=0o777, dir_fd=None)
    except FileExistsError:
        print("Директория уже существует")


def remove_directory(string):
    try:
        os.rmdir(full_path + string, dir_fd=None)

    except FileNotFoundError:
        print("Директория не найдена")


def change_current_dir(new_full_path):
    global full_path
    try:
        if new_full_path == ".":
            last_folder_name_length = len(full_path.split("\\")[-1])
            f = full_path[:len(full_path) - last_folder_name_length]
            os.chdir(f)

        else:
            os.chdir(full_path + new_full_path)

    except FileNotFoundError:
        print("Директория не найдена")

    finally:
        full_path = os.getcwd()
