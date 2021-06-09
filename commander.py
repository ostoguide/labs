import os
import shutil
import sys

x = str(input("Type \"Help\" to list available commands: "))
if x == "Help":
    print("Type \"read\" to open a direct file for reading")
    print("Type \"write\" to write(create) a direct file")
    print("Type \"mkdir\" to create a folder")
    print("Type \"rmdir\" to delete a folder")
    print("Type \"rename\" to rename a file")
    print("Type \"remove\" to delete a file")
    print("Type \"copy\" to copy a file")
    print("Type \"exit\" to shut down the program")
else:
    print("Ok, dude. So you mean that you need no help. Good luck.")
while True:
    com = str(input("Enter any command from the help list "))
    if com == "read":
        dir1 = str(input("Please enter the direct location. f.e: C://somedir/somefile.txt:\n"))
        if os.path.exists(dir1):
            print("File's successfully found")
            myfile = open(dir1, "r")
            myfile.close()
        else:
            print("Couldn't find the file")
    elif com == "write":
        dir1 = str(input("Please enter the direct location. f.e: C://somedir/somefile.txt:\n"))
        myfile = open(dir1, "w")
        myfile.close()
    elif com == "mkdir":
        dir1 = str(input("Please enter the directory + name. f.e: C://somedir/simplename:\n"))
        os.mkdir(dir1)
    elif com == "rmdir":
        dir1 = str(input("Please enter the directory of the folder. f.e: C://somedir/simplename:\n"))
        if os.path.exists(dir1):
            print("Path's successfully found")
            os.rmdir(dir1)
        else:
            print("Couldn't find the path")
    elif com == "rename":
        dir1 = str(input("Please enter the directory of the file. f.e: C://somedir/simplename:\n"))
        if os.path.exists(dir1):
            print("File's successfully found")
            newName = str(input("Please enter the directory + nem name of the file. f.e: C://somedir/simplename:\n"))
            os.rename(dir1, newName)
        else:
            print("Couldn't find the file")
    elif com == "remove":
        dir1 = str(input("Please enter the directory of the file. f.e: C://somedir/simplename:\n"))
        if os.path.exists(dir1):
            print("File's successfully found")
            os.remove(dir1)
        else:
            print("Couldn't find the file")
    elif com == "copy":
        dir1 = str(input("Please enter the directory of the file. f.e: C://somedir/simplename:\n"))
        if os.path.exists(dir1):
            print("File's successfully found")
            dir2 = str(input("Please enter the destination directory. f.e: C://somedir/simplename:\n"))
            if os.path.exists(dir2):
                print("Path's successfully found")
                shutil.copy(dir1, dir2)
            else:
                print("Couldn't find the path")
        else:
            print("Couldn't find the file")
    elif com == "Help":
        print("Type \"read\" to open a direct file for reading")
        print("Type \"write\" to write(create) a direct file")
        print("Type \"mkdir\" to create a folder")
        print("Type \"rmdir\" to delete a folder")
        print("Type \"rename\" to rename a file")
        print("Type \"remove\" to delete a file")
        print("Type \"copy\" to copy a file")
        print("Type \"exit\" to shut down the program")
    elif com == "exit":
        sys.exit()
    else:
        print("Unknown command, please type \"Help\" to list available commands: ")
