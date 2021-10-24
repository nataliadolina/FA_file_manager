from file_manager.dir_commands import create_directory, remove_directory, change_current_dir
from file_manager.file_commands import create_file, rename_file, delete_file, copy_file_to_folder, show_file_data, \
    move_file

commands = {"mkdir": create_directory, "rmdir": remove_directory, "cd": change_current_dir, "touch": create_file,
            "cat": show_file_data, "rm": delete_file, "cp": copy_file_to_folder, "mv": move_file, "rename": rename_file}
root = ""
full_path = ""


def parse(filename):
    with open("C:/Users/ACER/Desktop/FA/UNIX/FA_file_manager/file_manager/inputs/" + filename, 'rt',
              encoding="UTF-8") as file:  # указала абсолютный путь, так как в процессе корневая папка изменится
        lines = file.read().split("\n")
    return lines


def process_file(lines):
    for line in lines:
        command, *args = line.split()
        commands[command](args)


while True:
    if not root:
        root = input("Пожалуйста, введите имя файла с рабочей директорией. ")
        dir = parse(root)[0]
        commands["cd"]([dir])
    file_to_read = input("Пожалуйста, введите имя файла с данными. ")
    lines = parse(file_to_read)
    process_file(lines)
