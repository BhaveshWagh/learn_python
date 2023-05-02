def collapse(list):
    Nlist = []
    if len(list) % 2 == 0:
        for i in range(0, len(list), 2):
           list2 = list[i] + list[i + 1]
           Nlist.append(list2)
        return Nlist
    else:
        for j in range(0, len(list) - 1, 2):
            list3 = list[j] + list[j + 1]
            Nlist.append(list3)
        Nlist.append(list[-1])
        return Nlist
arr = [1,2,3,4,6,4,1]
print(collapse(arr))