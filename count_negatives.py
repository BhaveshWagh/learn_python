def count_negatives(lists):
    result = len(list(filter(lambda i : (i < 0),lists)))
    return result

lists = [1,-2,4,-3,12,-23]
print(count_negatives(lists))                                                               