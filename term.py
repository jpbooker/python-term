from sys import platform
import os

current_directory = ""
WIN32 = "win32"
NT = "NT"
LINUX = "linux"
LS = "ls"
CD = "cd"
PRINT = "print"
EXIT = "exit"

if platform == WIN32 or NT:
    current_directory = "C:/"
elif LINUX in platform:
    current_directory = "/"

def list_files(directory):
    if LS in directory:
        dir_list = os.listdir(directory.replace("ls ", ""))
        for each in dir_list:
            print(each)
    else:
        dir_list = os.listdir(current_directory)
        for each in dir_list:
            print(each)

def change_dir(directory):
    directory = directory.replace("cd ", "")
    if directory != "":
        global current_directory

        if directory[0] == "/":
            if os.path.exists(directory[1:]):
                current_directory = directory[1:]
        elif directory == "..":
            split_path = current_directory.split("/")
            split_path.remove(split_path[-1])
            current_directory = ""
            for each in split_path:
                current_directory += each
                current_directory += "/"
        elif os.path.exists(current_directory + directory):
            current_directory += directory
        else:
            print("dir does't exist")
            
while True:
    command = input(current_directory + " $ ")

    if PRINT in command:
        print(command.replace("print ", ""))

    if LS in command:
        list_files(command)

    if CD in command:
        change_dir(command)

    if command == EXIT:
        exit()
