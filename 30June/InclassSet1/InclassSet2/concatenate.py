def add_lists(list1, list2):
    list = []
    min = min(len(list1), len(list2))

    for i in range(min):
        list.append(list1[i] + list2[i])

    if len(list1) > len(list2):
        list.extend(list1[min:])
    else:
        list.extend(list2[min:])

    return list

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = add_lists(list1, list2)

print(new_list)
