def all_less(list1, list2):
    if len(list1) != len(list2):
        return False
    length = len(list1)
    for i in range(length):
        if list1[i] > list2[i]:
            return False
    return True