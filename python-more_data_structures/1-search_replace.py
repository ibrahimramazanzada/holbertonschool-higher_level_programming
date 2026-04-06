#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_List = []
    for i in my_list:
        if i == search:
            new_List.append(replace)
        else:
            new_List.append(i)
    return new_List
