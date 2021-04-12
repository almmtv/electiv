import os
import sys


def solve(directory, text, is_recursive, depth):
    list_of_all = []
    cur_dir = os.getcwd()
    os.chdir(directory)
    if not is_recursive:
        for i in os.walk('.'):
            list_of_all += [i]
            break
    else:
        for current_dir, dirs, files in os.walk('.'):
            if len(current_dir.split('/')) > depth:
                pass
            else:
                list_of_all += [(current_dir, dirs, files)]
    list_of_file_addresses = []
    for address, dirs, files in list_of_all:
        for file in files:
            list_of_file_addresses += [str(address + "/" + file)]
    result = []
    for file in list_of_file_addresses:
        with open(file) as current_file:
            try:
                if text in current_file.read():
                    result += [file]
            except UnicodeError:
                pass
    os.chdir(cur_dir)
    return result


if __name__ == "__main__":
    search_text = sys.argv[-2]
    path = sys.argv[-1]
    in_depth = 0
    is_recursive_ = False
    if '-r' in sys.argv:
        is_recursive_ = True
    if '-d' in sys.argv:
        in_depth += int(sys.argv[sys.argv.index('-d') + 1])
    if not is_recursive_:
        in_depth = 0
    res = solve(path, search_text, is_recursive_, in_depth)
    print(res)
