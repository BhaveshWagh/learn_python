def sum(list1,target):
    for i in range(0,len(list1)):
        result = list1[i] + list1[i + 1]
        # print("***",result)
        if target == result:
            return list1.index(list1[i]),list1.index(list1[i+1])
    else:
        return False

list1 = [3,3,3,4,5]
print(sum(list1, 6))


