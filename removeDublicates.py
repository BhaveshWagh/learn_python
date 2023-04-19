
def removeDublicates(array):
    uniqueArr = []
    for i in array:
        if i not in uniqueArr:
            uniqueArr.append(i)
    return uniqueArr
arr = [1,2,3,4,3,5,3,4,3]
print(removeDublicates(arr))

# this will not work this uncompleted

# def removeDublicates(array):
#     uniqueArr = []
#     for i in range(len(array) - 1):
#         for j in range(len(array)-1):
#             if (array[i] != array[j]):
#                 uniqueItem = array[i]
#                 uniqueArr.append(uniqueItem)
#     return uniqueArr
