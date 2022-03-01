def is_1_to_1(dictionary):

    if len(dictionary) == 0:
        return True

    value_set = set()

    for key in dictionary.keys():
        value = dictionary[key]
        if value in value_set:
            return False
        else:
            value_set.add(value)

    return True