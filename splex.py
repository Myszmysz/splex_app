#! python3
# splex.py - Application for splitting common expenses within a group.

import sys
import os


# todo save splex to file
# todo read splex from file

def list_of_files():
    return [name.rstrip(".csv") for name in os.listdir(r"E:\stuff\Maciej\_PYTHON\apps\splex_app\data")]


def menu():
    # todo read list of files

    command = sys.argv[1]
    if command == "new":
        None
        # todo create new splex
    if command == "open":
        None
        # todo open existing splex
    if command == "list":
        # print list of splex files
        lof = list_of_files()
        if lof:
            print(*lof, sep="\n")
        else:
            print("No splex files found!")
    if command == "delete":
        None
        # todo delete splex
    if command in list_of_files():
        # todo add new record
        # todo calculate result


menu()
