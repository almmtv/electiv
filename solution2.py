import os
import sys


def solve(directory, size, is_recursive, is_greater, is_sorted):
    list_of_all = []
    if not is_recursive:
        for i in os.walk(directory):
            list_of_all += [i]
            break
    else:
        for current_dir, dirs, files in os.walk(directory):
            list_of_all += [(current_dir, dirs, files)]
    list_of_file_addresses = []
    for address, dirs, files in list_of_all:
        for file in files:
            list_of_file_addresses += [str(address + "/" + file)]
    new_dict = {}
    result = []
    for file in list_of_file_addresses:
        file_size = os.path.getsize(file)
        if is_greater:
            if file_size > size:
                if file_size in new_dict:
                    new_dict[file_size] += [file]
                else:
                    new_dict[file_size] = [file]
        else:
            if 0 < file_size <= size:
                if file_size in new_dict:
                    new_dict[file_size] += [file]
                else:
                    new_dict[file_size] = [file]
    if is_sorted:
        list_keys = list(new_dict.keys())
        list_keys.sort()
        for i in list_keys:
            for j in new_dict[i]:
                result += [(j, i)]
    else:
        for i in new_dict:
            for j in new_dict[i]:
                result += [(j, i)]
    return result


if __name__ == "__main__":
    search_size = int(sys.argv[-2])
    path = sys.argv[-1]
    is_recursive_ = False
    is_greater_ = False
    is_sorted_ = False
    if '-r' in sys.argv:
        is_recursive_ = True
    if '-g' in sys.argv:
        is_greater_ = True
    if '-s' in sys.argv:
        is_sorted_ = True
    res = solve(path, search_size, is_recursive_, is_greater_, is_sorted_)
    print(res)