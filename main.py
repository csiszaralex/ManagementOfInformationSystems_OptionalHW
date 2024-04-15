import os
import re

# The function names to search for
dict: list[str] = ["main", "for"] #TODO modify me
# The functions that are found
found: set[str] = set()
# The directory to search for .c files
directory: str = os.getcwd()
# The regex to search for functions
regex = re.compile("^\\w* \\w* ?\\(.*\\) ?{?}?$")


def search_c_files(directory: str) -> None:
    """
    Walk through the directory and search for .c files.
    If a .c file is found, call list_functions() on it.
    Parameters:
        directory (str): The directory to search for .c files
    """
    for file in os.listdir(directory):
        if file.endswith(".c"):
            path = os.path.join(directory, file)
            collect_functions(path)
        elif os.path.isdir(os.path.join(directory, file)):
            search_c_files(os.path.join(directory, file))


def collect_functions(file_path: str) -> None:
    """
    Read the file and search for functions.
    If a function is found, check if it is in the dictionary.
    If it is, add it to the set.
    Parameters:
        file_path (str): The path to the file to search for functions
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if regex.match(line):
                func = line.split(" ")[1].split("(")[0]
                if func in dict:
                    found.add(func)


search_c_files(directory)
for i in found:
    print(i)
