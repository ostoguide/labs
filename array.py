import numpy as np
import random
import string
import time
import os
import sys


def intArr():
    start_time = time.time()
    arr = np.random.randint(99, size=size)
    print(arr)
    with open("stats.txt", "a")as f:
        f.write("Type: int\n")
        f.write("Size: ")
        f.write(str(size) + "\n")
        f.write("Time: ")
        f.write(str(time.time() - start_time))
        f.write("s\n")
    print("Time: ", time.time() - start_time, "s")


def floatArr():
    start_time = time.time()
    arr = np.random.random((size,))
    print(arr)
    f = open("stats.txt", "a")
    f.write("Type: float\n")
    f.write("Size: ")
    f.write(str(size) + "\n")
    f.write("Time: ")
    f.write(str(time.time() - start_time))
    f.write("s")
    print("Time: ",time.time() - start_time, "s")


def strArray():
    start_time = time.time()
    letter = string.ascii_letters
    arr = []
    i = 0
    while i < size:
        item = random.choice(letter)
        arr.append(item)
        i += 1
    print(arr)
    f = open("stats.txt", "a")
    f.write("Type: str\n")
    f.write("Size: ")
    f.write(str(size) + "\n")
    f.write("Time: ")
    f.write(str(time.time() - start_time))
    f.write("s")
    print("Time: ",time.time() - start_time, "s")


def mixArr():
    start_time = time.time()
    arr2 = np.random.randint(-20,20,size=10)
    letter = string.ascii_letters
    arr = []
    i = 0
    while i < size:
        item = random.choice(letter)
        arr.append(item)
        num = random.choice(arr2)
        arr.append(num)
        i += 1
    print(arr)
    f = open("stats.txt", "a")
    f.write("Type: mixed\n")
    f.write("Size: ")
    f.write(str(size) + "\n")
    f.write("Time: ")
    f.write(str(time.time() - start_time))
    f.write("s")
    print("Time: ",time.time() - start_time, "s")


while True:
    choice1 = input(str("Choose the size of array: 1-10, 2-100, 3-1000, 4-10000, 5-1000000000 or type \"exit\" to finish process: "))
    if choice1 == "1":
        print("Size 10")
        choice2 = input(str("Choose the type of array: 1-int, 2-float, 3-str, 4-mixed: "))
        if choice2 == "1":
            print("Type int")
            size = 10
            intArr()
        elif choice2 == "2":
            print("Type float")
            size = 10
            floatArr()
        elif choice2 == "3":
            print("Type str")
            size = 10
            strArray()
        elif choice2 == "4":
            print("Type mixed")
            size = 10
            mixArr()
        else:
            print("Incorrect input. Please choose one of the given types: ")
    elif choice1 == "2":
        print("Size 100")
        choice2 = input(str("Choose the type of array: 1-int, 2-float, 3-str, 4-mixed: "))
        if choice2 == "1":
            print("Type int")
            size = 100
            intArr()
        elif choice2 == "2":
            print("Type float")
            size = 100
            floatArr()
        elif choice2 == "3":
            print("Type str")
            size = 100
            strArray()
        elif choice2 == "4":
            print("Type mixed")
            size = 100
            mixArr()
        else:
            print("Incorrect input. Please choose one of the given types: ")
    elif choice1 == "3":
        print("Size 1000")
        choice2 = input(str("Choose the type of array: 1-int, 2-float, 3-str, 4-mixed: "))
        if choice2 == "1":
            print("Type int")
            size = 1000
            intArr()
        elif choice2 == "2":
            print("Type float")
            size = 1000
            floatArr()
        elif choice2 == "3":
            print("Type str")
            size = 1000
            strArray()
        elif choice2 == "4":
            print("Type mixed")
            size = 1000
            mixArr()
        else:
            print("Incorrect input. Please choose one of the given types: ")
    elif choice1 == "4":
        print("Size 10000")
        choice2 = input(str("Choose the type of array: 1-int, 2-float, 3-str, 4-mixed: "))
        if choice2 == "1":
            print("Type int")
            size = 10000
            intArr()
        elif choice2 == "2":
            print("Type float")
            size = 10000
            floatArr()
        elif choice2 == "3":
            print("Type str")
            size = 10000
            strArray()
        elif choice2 == "4":
            print("Type mixed")
            size = 10000
            mixArr()
        else:
            print("Incorrect input. Please choose one of the given types: ")
    elif choice1 == "5":
        print("Size 1000000000")
        choice2 = input(str("Choose the type of array: 1-int, 2-float, 3-str, 4-mixed: "))
        if choice2 == "1":
            print("Type int")
            size = 1000000000
            intArr()
        elif choice2 == "2":
            print("Type float")
            size = 1000000000
            floatArr()
        elif choice2 == "3":
            print("Type str")
            size = 1000000000
            strArray()
        elif choice2 == "4":
            print("Type mixed")
            size = 1000000000
            mixArr()
        else:
            print("Incorrect input. Please choose one of the given types: ")
    elif choice1 == "exit":
        f = open("stats.txt", "w")
        f.close()
        exit(0)
        sys.exit
        os.abort()
    else:
        print("Incorrect input. Please choose one of the given sizes: ")
