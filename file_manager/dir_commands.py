import os
from file_manager.settings import path

def create_directory(string):
    string = string[0]
    try:
        os.mkdir(path.get_full_path() + string, mode=0o777, dir_fd=None)
    except FileExistsError:
        print("Директория уже существует")


def remove_directory(string):
    string = string[0]
    try:
        os.rmdir(path.get_full_path() + string, dir_fd=None)

    except FileNotFoundError:
        print("Директория не найдена")


def change_current_dir(new_full_path):
    new_full_path = new_full_path[0]
    global path
    full_path = path.get_full_path()
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
        path.set_full_path(os.getcwd())
