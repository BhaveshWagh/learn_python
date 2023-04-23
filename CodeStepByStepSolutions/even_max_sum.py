def even_sum_max():
    list = []
    even_list = []
    even_sum = 0
    Total_no = int(input("how many integers? "))

    for i in range(Total_no):
        No = int(input("next integer? "))
        list.append(No)
        if list[i] % 2 == 0:
            even_sum += list[i]
            even_list.append(list[i])
# print(even_list)
    print("even sum =", even_sum)
    print("even max =",max(even_list))


# how many integers? 4
# next integer? 2
# next integer? 9
# next integer? 18
# next integer? 4
# even sum = 24
# even max = 18
