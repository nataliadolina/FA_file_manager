import os
from file_manager.settings import path


def to_dir(string):
    if string[0] != "/":
        string = "/" + string

    return string


def read_file_data(filename):
    with open(path.get_full_path() + to_dir(filename), "rt", encoding="UTF-8") as file:
        return file.read()


def write_file_data(filename, data):
    with open(path.get_full_path() + to_dir(filename), "wt", encoding="UTF-8") as file:
        file.write(data)


def create_file(args):
    filename = args[0]
    with open(filename, mode="w+"):
        print("New file created!")


def show_file_data(filename):
    # with open(path.get_full_path() + filename, "rt") as file:
    #    for row in file:
    data = read_file_data(filename[0])
    print(data)


def delete_file(filename):
    os.remove(path.get_full_path() + to_dir(filename[0]))


def move_file(filename_dir):
    filename, dir = filename_dir
    filename = to_dir(filename)
    full_path = path.get_full_path()
    os.replace(full_path + filename, full_path + dir + filename)


def copy_file_to_folder(filename_dir):
    filename, dir = filename_dir

    data = read_file_data(filename)  # считываем данные из файла, который хотим копировать
    move_file([filename, dir])  # перемещаем файл в папку, куда хотим копировать
    write_file_data(filename, data)  # восстанавливаем перемещённый файл в прошлой директории


def rename_file(filename_new_filename):
    filename, new_filename = filename_new_filename
    os.rename(path.get_full_path() + to_dir(filename), path.get_full_path() + to_dir(new_filename))
