#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""

        new_list = []
    for item in my_list :
        if (item == search):
            item = replace
            new_list.append(item)
        else:
            new_list.append(item)
    return(new_list)
